from dash import html, dcc
from src.clinical_policy import CLINICAL_CONTEXTS
from src.data_loader import load_data

df = load_data()

def create_layout():
    return html.Div(
        style={"maxWidth": "1200px", "margin": "0 auto", "padding": "20px"},
        children=[

            html.H2(
                "Sistema Inteligente de Apoio ao Diagnóstico",
                style={"textAlign": "center"}
            ),
            html.P(
                "Ferramenta de suporte à decisão clínica. "
                "Não substitui avaliação médica.",
                style={"textAlign": "center", "color": "gray"}
            ),

            html.Hr(),

            # 🔷 GRID SUPERIOR
            html.Div(
                style={
                    "display": "grid",
                    "gridTemplateColumns": "repeat(auto-fit, minmax(320px, 1fr))",
                    "gap": "20px"
                },
                children=[

                    # CONTEXTO CLÍNICO
                    html.Div(
                        style={
                            "border": "1px solid #ddd",
                            "borderRadius": "12px",
                            "padding": "15px"
                        },
                        children=[
                            html.H4("Contexto Clínico de Uso"),
                            dcc.Dropdown(
                                id="clinical-context",
                                options=[{"label": k, "value": k} for k in CLINICAL_CONTEXTS],
                                placeholder="Selecione o contexto clínico",
                                clearable=False
                            ),
                            html.Br(),
                            html.Div(id="clinical-tooltip")
                        ]
                    ),

                    # PACIENTE
                    html.Div(
                        style={
                            "border": "1px solid #ddd",
                            "borderRadius": "12px",
                            "padding": "15px"
                        },
                        children=[
                            html.H4("Paciente"),
                            dcc.Dropdown(
                                id="patient-id",
                                options=[{"label": f"Paciente {i}", "value": i} for i in range(len(df))],
                                placeholder="Selecione o paciente",
                                clearable=False
                            ),
                            html.Br(),
                            html.Button(
                                "Gerar Análise Clínica",
                                id="run-analysis",
                                disabled=True,
                                style={"width": "100%", "padding": "10px", "fontSize": "16px", "cursor": "pointer"}
                            )
                        ]
                    )
                ]
            ),

            html.Br(),

            # 🔷 LOCAL STORAGE
            dcc.Store(id="stored-analysis", storage_type="local"),

            # 🔷 ÁREA DE RESULTADO COM LOADING
            dcc.Loading(
                id="loading-analysis",
                type="circle",
                children=html.Div(
                    id="analysis-output",
                    style={
                        "border": "1px dashed #ccc",
                        "borderRadius": "12px",
                        "padding": "20px",
                        "minHeight": "150px",
                        "textAlign": "center",
                        "color": "gray",
                        "width": "100%",
                        "boxSizing": "border-box",
                        "overflow": "hidden"
                    },
                    children=[
                        # Título paciente + botão, inicialmente oculto
                        html.Div(
                            id="patient-header",
                            style={
                                "display": "none",
                                "justifyContent": "space-between",
                                "alignItems": "center",
                                "marginBottom": "15px",
                                "fontWeight": "bold"
                            },
                            children=[
                                html.Div(id="current-patient", style={"textAlign": "center"}),
                                html.Button(
                                    "Limpar Resultado",
                                    id="clear-result",
                                    n_clicks=0,
                                    style={"padding": "5px 10px", "cursor": "pointer", "fontSize": "14px"}
                                )
                            ]
                        ),
                        # Container para cards e gráficos
                        html.Div(
                            id="results-container",
                            children=[
                                html.Div(
                                    "Nenhum paciente selecionado. Selecione contexto e paciente, depois clique em 'Gerar Análise Clínica'.",
                                    style={"color": "gray", "textAlign": "center"}
                                )
                            ]
                        )
                    ]
                )
            )
        ]
    )
