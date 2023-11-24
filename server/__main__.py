#!/usr/bin/env python3

import connexion

from server.config.json_provider import CustomJSONProvider
from server.exceptions import NotFoundException, not_found_handler


def main():
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('swagger.yaml', arguments={'title': 'Simple Recipe Generator - ML'}, pythonic_params=True)
    app.app.json = CustomJSONProvider(app.app)
    app.add_error_handler(NotFoundException, not_found_handler)
    app.run(port=8080)


if __name__ == '__main__':
    main()
