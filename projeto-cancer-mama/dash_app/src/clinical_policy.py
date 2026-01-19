CLINICAL_CONTEXTS = {
    "Triagem Inicial": {
        "threshold": 0.40,
        "label": "Alta sensibilidade",
        "description": (
            "Indicada para triagem inicial e populações de alto risco. "
            "Prioriza a detecção precoce, reduzindo falsos negativos."
        ),
        "color": "#d62728"
    },
    "Atendimento Ambulatorial": {
        "threshold": 0.50,
        "label": "Equilíbrio clínico",
        "description": (
            "Uso ambulatorial padrão. "
            "Equilíbrio entre sensibilidade e precisão."
        ),
        "color": "#ff7f0e"
    },
    "Exames Invasivos / Alto Custo": {
        "threshold": 0.70,
        "label": "Abordagem conservadora",
        "description": (
            "Indicado para exames invasivos ou caros. "
            "Reduz alarmes falsos."
        ),
        "color": "#1f77b4"
    },
    "Confirmação Diagnóstica": {
        "threshold": 0.85,
        "label": "Alta precisão",
        "description": (
            "Confirmação final ou ambientes com recursos limitados."
        ),
        "color": "#2ca02c"
    }
}
