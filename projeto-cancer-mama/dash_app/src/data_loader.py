import pandas as pd
from sklearn.datasets import load_breast_cancer

def load_data():
    data = load_breast_cancer(as_frame=True)
    df = data.frame
    df["target"] = data.target
    return df
