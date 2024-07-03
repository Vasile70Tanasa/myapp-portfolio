from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import requests

def home(request):
    """
    Render the home page.
    """
    return render(request, "pages/home.html", {})

# @method_decorator(csrf_exempt, name='dispatch')


# def post(self, request, *args, **kwargs):
#     message = request.POST.get('message')
#     if not message:
#         return JsonResponse({'error': 'No message provided'}, status=400)
#
#     try:
#         response.raise_for_status()  # Raise an error for bad status codes
#         return JsonResponse(response.json(), safe=False)
#     except requests.RequestException as e:
#         return JsonResponse({'error': str(e)}, status=500)
#
# """
# """

