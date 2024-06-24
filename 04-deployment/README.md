## Deployment

Deployment is done with Docker.

There are three ways to deploy a machine learning model.

- web service
- streaming
- batch

### Web service

An API for machine learning model is deployed.

### Batch

In this work, I predict the scores in batches. 

### Docker Setup

```
FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY "scoring.py" .
```
<br>
Firsly, docker image named `scoring-image` is built.

```
docker build -t scoring-image .

```

Then, the docker container is run with this command.

```
docker run scoring-image python scoring.py arg1 arg2

```
The year and month we want to predict will need to be written in arg1 and arg2 respectively.
