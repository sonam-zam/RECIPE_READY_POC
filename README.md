# Recipe Generator Using ML

## Overview
A server to generate and manipulate cooking recipes using HuggingFaces T5 recipe generation model. 
Project uses **Transformers** to provide ML support and **Connexion** with **Flask** for the REST API. 

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m server
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