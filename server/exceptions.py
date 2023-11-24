from connexion.lifecycle import ConnexionResponse


class NotFoundException(RuntimeError):
    """Not found"""


def not_found_handler(request, error):
    return ConnexionResponse(
        body='Item not found on the server',
        status_code=404,
        mimetype="application/json",
        headers=None)
