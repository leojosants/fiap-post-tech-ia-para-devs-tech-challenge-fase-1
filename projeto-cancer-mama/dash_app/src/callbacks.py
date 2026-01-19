from dash import Input, Output, State, html, no_update, dcc, callback_context
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

from src.data_loader import load_data
from src.model import load_model, predict_proba
from src.clinical_policy import CLINICAL_CONTEXTS

# 🎨 COR ÚNICA PARA O PACIENTE (Não conflita com as suas 4 cores)
COLOR_PATIENT = "#9467bd"  # Roxo/Violeta

def register_callbacks(app):
    df = load_data()
    model = load_model()

    @app.callback(
        Output("results-container", "children"),
        Output("run-analysis", "disabled"),
        Output("clinical-context", "value"),
        Output("patient-id", "value"),
        Output("stored-analysis", "data"),
        Output("patient-header", "style"),
        Output("current-patient", "children"),
        Input("run-analysis", "n_clicks"),
        Input("clinical-context", "value"),
        Input("patient-id", "value"),
        Input("clear-result", "n_clicks"),
        State("stored-analysis", "data"),
        prevent_initial_call=False
    )
    def handle_ui(n_clicks, context_key, patient_index, clear_clicks, stored_data):
        trigger = callback_context.triggered[0]["prop_id"] if callback_context.triggered else None
        
        # 1. LÓGICA DO BOTÃO "GERAR"
        # Deve estar desativado se: (Campos vazios) OU (Já houver resultado na tela)
        inputs_filled = context_key is not None and patient_index is not None
        has_result_on_screen = stored_data is not None
        btn_disabled = not (inputs_filled and not has_result_on_screen)

        # ---------------------------------------------------------------------
        # 🔹 GATILHO: LIMPAR (Reseta tudo)
        if trigger == "clear-result.n_clicks":
            return (
                html.Div("Nenhum paciente selecionado. Selecione contexto e paciente.", style={"color": "gray"}), 
                True, None, None, None, {"display": "none"}, ""
            )

        # 🔹 GATILHO: MUDANÇA NOS DROPDOWNS
        if trigger in ["clinical-context.value", "patient-id.value"]:
            # Se mudou os campos mas não limpou a tela, o botão continua desativado
            return (no_update, btn_disabled, no_update, no_update, no_update, no_update, no_update)

        # 🔹 GATILHO: INICIALIZAÇÃO OU CLIQUE EM GERAR
        target_idx = stored_data["patient_index"] if (trigger is None and stored_data) else patient_index
        target_ctx = stored_data["context_key"] if (trigger is None and stored_data) else context_key

        if (trigger == "run-analysis.n_clicks" or (trigger is None and stored_data)) and target_idx is not None:
            patient_row = df.iloc[[target_idx]].drop(columns=["target"])
            probability = predict_proba(model, patient_row)
            policy = CLINICAL_CONTEXTS[target_ctx]
            threshold = policy["threshold"]
            
            decision = "Indícios de Tumor Maligno" if probability >= threshold else "Baixa probabilidade de malignidade"
            now_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            # Card de Resultado
            result_card = html.Div(className="box fade-in", children=[
                html.H4(f"Análise: {target_ctx}"),
                html.P(decision, style={"fontSize": "22px", "fontWeight": "bold", "color": policy["color"]}),
                html.P(f"Risco calculado pela IA: {probability:.1%}"),
            ])
            
            # Gráfico 1: Indicador (Sempre Roxo para o paciente)
            risk_fig = go.Figure(go.Bar(
                x=[probability], y=["Paciente"], orientation="h",
                marker_color=COLOR_PATIENT, text=[f"{probability:.1%}"], textposition="inside"
            ))
            risk_fig.update_layout(xaxis=dict(range=[0,1], tickformat=".0%"), title="Risco Estimado do Paciente", height=200)

            # Gráfico 2: Comparação (Roxo vs Cor do Contexto)
            compare_fig = px.bar(
                x=["Sua Probabilidade", f"Limiar ({policy['label']})"], 
                y=[probability, threshold],
                text=[f"{probability:.1%}", f"{threshold:.1%}"],
                title="Comparação com Protocolo Clínico"
            )
            compare_fig.update_traces(marker_color=[COLOR_PATIENT, policy["color"]], textposition="outside")
            compare_fig.update_layout(yaxis=dict(range=[0,1], tickformat=".0%"), height=300)
            
            new_storage = {"patient_index": target_idx, "context_key": target_ctx}
            
            return [result_card, dcc.Graph(figure=risk_fig), dcc.Graph(figure=compare_fig)], \
                   True, no_update, no_update, new_storage, \
                   {"display": "flex", "justifyContent": "space-between"}, \
                   f"Paciente {target_idx} - Processado em {now_str}"

        return no_update, btn_disabled, no_update, no_update, stored_data, no_update, ""