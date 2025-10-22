from django.http import JsonResponse

def custom_404(request, exception):
    return JsonResponse({
        "error": "Ops... Something wrong happened :/",
        "status_code": 404
    }, status=404)

def custom_500(request):
    return JsonResponse({
        "error": "Server Error, Please check back later.",
        "status_code": 500
    }, status=500)