import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from scipy.stats import zscore


def zscore_anomaly_detection(df, threshold=3):
    z_scores = np.abs(zscore(df))
    return (z_scores > threshold).any(axis=1)


def isolation_forest_detection(df, contamination=0.01):
    model = IsolationForest(contamination=contamination, random_state=42)
    preds = model.fit_predict(df)
    return preds, model.decision_function(df)


def lof_detection(df, contamination=0.01):
    lof = LocalOutlierFactor(contamination=contamination)
    preds = lof.fit_predict(df)
    return preds
