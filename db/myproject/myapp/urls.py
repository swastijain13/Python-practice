from django.http import JsonResponse


def home_view(request):
    return JsonResponse({"message": "Welcome to My project!!"})

