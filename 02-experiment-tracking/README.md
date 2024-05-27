## Experiment Tracking

It is difficult to track manually if we are training a large amount of data and models. Therefore, we got a tool to solve this problem. That is `mlflow`.

## MLflow

#### MLflow server setup

To start mlflow ui, if you already have mlflow.db started, firstly go into the file where mlflow.db exists. If not, go into the file path where you want to keep mlflow.db

```
mlflow ui --backend-store-uri sqlite:///mlflow.db

```

#### MLflow experiment setup

In Jupyter notebook, we can start mlflow like this. 
`
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("nyc-taxi-experiment")
`

#### MLflow setting tags, logging params, metrics and artifact
When we train the model, we can start with `mlflow.start_run()`.

```
with mlflow.start_run():
    mlflow.set_tag("tag_name", "tag_value")
    #model training logic here
    mlflow.log_param("param_name", "param_value")
    mlflow.log_metric("metric_name", "metric_value")

    mlflow.log_artifact(local_path="", artifact_path="")
```

or we can also use autolog. With autolog, we do not need to manually track parameters and metrics.<br>

```
mlflow.autolog()
with mlflow.start_run():
    #model training logic here
```

With `mlflow.autolog()` sometimes, there might be errors like not tracking datasets properly. We can bypass that by passing parameters in autolog like `mlflow.sklearn.autolog(log_datasets = False)` or find the root problems. 
<br><br>
For paramter, we should log parameters for machine learning as well as dataset path for data versioning purpose.<br><br>

We can log artifact, and save the model in mlflow. That way, we can track the model version with corresponding metrics and parameters.

We can find the best model with `MlflowClient`.
```
client = MlflowClient()

# Retrieve the top_n model runs and log the models
experiment = client.get_experiment_by_name(EXPERIMENT_NAME)
runs = client.search_runs(
    experiment_ids=experiment.experiment_id,
    run_view_type=ViewType.ACTIVE_ONLY,
    max_results=top_n,
    order_by=["metrics.rmse ASC"]
    )
#from top 5 run we can get best run with runs[0]
best_run = runs[0]
model_uri = f"runs:/{best_run.info.run_id}/model"
model_name = "A Cool Name"
mlflow.register_model(model_uri=model_uri, name=model_name)
```
We can register best model with `mlflow.register_model(model_uri=model_uri, name=model_name)`. 

