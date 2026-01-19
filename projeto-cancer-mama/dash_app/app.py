
import os
from dash import Dash
from src.layout import create_layout
from src.callbacks import register_callbacks

app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "Sistema de Apoio ao Diagnóstico"

app.layout = create_layout()
register_callbacks(app)

# 🚨 NECESSÁRIO PARA O HUGGING FACE
server = app.server

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 7860)),
        debug=False
    )