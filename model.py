import pandas as pd
import mlflow
import joblib
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, f1_score, classification_report, ConfusionMatrixDisplay

from train import Nome_do_experimento, Versao_do_dataset

mlflow.set_tracking_uri("http://mlflow:5000")
mlflow.set_experiment(Nome_do_experimento)

with mlflow.start_run():
    print("Iniciando o treinamento...")
    wine = pd.read_csv("wine_data.csv")
    X = wine.drop("target", axis=1)
    y = wine["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = rfc(n_estimators=50, random_state=12)
    model.fit(X_train, y_train)

    model_filename = "random_forest.joblib"
    joblib.dump(model, model_filename)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    print("Logando artefatos no MLFLow...")

    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("random_state", 42)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("recall", recall)
    mlflow.log_metric("f1_score", f1)

    print("Logando o Modelo em Joblib no MLFlow...")
    mlflow.log_artifact(model_filename)

    mlflow.set_tag("dataset_version", Versao_do_dataset)

    cm_display = ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
    mlflow.log_figure(cm_display.figure_, "confusion_matrix.png")