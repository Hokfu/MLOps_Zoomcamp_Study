## Experiment Tracking

It is difficult to track manually if we are training a large amount of data and models. Therefore, we got a tool to solve this problem. That is `mlflow`.

## Mlflow

#### mlflow server setup

To start mlflow ui, if you already have mlflow.db started, firstly go into the file where mlflow.db exists. If not, go into the file path where you want to keep mlflow.db

```
mlflow ui --backend-store-uri sqlite:///mlflow.db

```

#### mlflow experiment setup

In Jupyter notebook, we can start mlflow like this. 
`
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("nyc-taxi-experiment")
`

#### mlflow setting tags, logging params, metrics and artifact
When we train the model, we can start with `mlflow.start_run()`.

```
with mlflow.start_run():
    mlflow.set_tag("tag_name", "tag_value")
    #model training logic here
    mlflow.log_param("param_name", "param_value")
    mlflow.log_metric("metric_name", "metric_value")

    mlflow.log_artifact(local_path="", artifact_path="")
```

For paramter, we should log parameters for machine learning as well as dataset path for data versioning purpose.<br><br>

We can log artifact, and save the model in mlflow. That way, we can track the model version with corresponding metrics and parameters.



