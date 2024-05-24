## Experiment Tracking

It is difficult to track manually if we are training a large amount of data and models. Therefore, we got a tool to solve this problem. That is `mlflow`.

### mlflow server setup 

To start mlflow ui, 
```
mlflow ui --backend-store-uri sqlite:\\\mlflow.db

```

In Jupyter notebook, we can start mlflow like this. 
`
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("nyc-taxi-experiment")
`

When we train the model, we can start with `mlflow.start_run()`.

```
with mlflow.start_run():
    mlflow.set_tag("tag_name", "tag_value")
    #model training logic here
    mlflow.log_param("param_name", "param_value")
    mlflow.log_metric("metric_name", "metric_value")
```

For paramter, we should log parameters for machine learning as well as dataset path for data versioning purpose.