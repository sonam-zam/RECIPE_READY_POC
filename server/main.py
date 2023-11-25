#!/usr/bin/env python3

import connexion
import uvicorn

from server.config.json_provider import CustomJSONProvider
from server.exceptions import NotFoundException, not_found_handler

app = connexion.FlaskApp(__name__, specification_dir='swagger/')
app.add_api('swagger.yaml', arguments={'title': 'Simple Recipe Generator - ML'}, pythonic_params=True)
app.app.json = CustomJSONProvider(app.app)
app.add_error_handler(NotFoundException, not_found_handler)

if __name__ == '__main__':
    uvicorn.run("server.main:app", port=8080, log_level="debug")
