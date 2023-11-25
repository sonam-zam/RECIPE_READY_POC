# Recipe Generator Using ML

## Overview
A server to generate and manipulate cooking recipes using a T5 recipe generation model. 
Project uses Hugging Face **[Transformers](https://huggingface.co/docs/transformers/index)** to provide ML support and 
**[Connexion](https://connexion.readthedocs.io/en/latest/)** 
with **[Flask](https://flask.palletsprojects.com/en/3.0.x/)** for the REST API. 

## Requirements
Python 3.11.6+, DynamoDB

## Setting up DynamoDB

If you are running the project locally, you need to set up **Dynamodb local** using any method described 
[here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html) and create an empty 
table with the name `recipe` and a composite primary key `{id: string, title: string}`.

When using **AWS DynamoDB** service, `base_repository.py` should be changed accordingly.

```python
self.dynamodb = boto3.resource('dynamodb')
```

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
uvicorn server.main:app --port 8080 --
```

and open your browser on URL:

```
http://localhost:8080/MARIADONA8019/recepe-generator-ML/1.0.0/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/MARIADONA8019/recepe-generator-ML/1.0.0/swagger.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t server .

# starting up a container
docker run -p 8080:8080 server
```

## Running on AWS 


### Configuring AWS services ###
The project uses **AWS Boto3** Python SDK, and it requires an access key. Refer to 
[this](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html) document on 
how to use `aws configure` command to generate auth credentials on your EC2 instance

### Launching service ###
To access the REST API using a client such as **Postman**, first the application should be allowed access to incoming requests 
from port 80 on the EC2 instance and an **NGINX** reverse proxy should be configured as mentioned
in [this](https://aws.plainenglish.io/deploying-a-flask-application-on-ec2-54cfeb396fa1) article.

This project uses **Uvicorn** instead of **Gunicorn** and the service definition needs to be changed as required.
```
http://<EC2-Public-IP>/MARIADONA8019/recepe-generator-ML/1.0.0/ui
```

Please note that everytime the EC2 instance is stopped and re-started, the public IP changes unless you have configured 
an **AWS Elastic IP**.