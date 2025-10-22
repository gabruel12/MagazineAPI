from rest_framework.views import exception_handler
from rest_framework.exceptions import NotFound, ValidationError, PermissionDenied
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, NotFound):
            response.data = {
                "error": "The requested resource was not found.",
                "status_code": 404
            }
        elif isinstance(exc, ValidationError):
            response.data = {
                "error": "Invalid JSON data.",
                "detalhes": response.data,
                "status_code": 400
            }
    else:
        return Response({
            "error": "Server Error.",
            "status_code": 500
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response