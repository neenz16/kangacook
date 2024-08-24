from django.shortcuts import render
from django.http import JsonResponse
from .models import Subscriber
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def submit_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email', '')
        if email:
            subscriber, created = Subscriber.objects.get_or_create(email=email)
            if created:
                return JsonResponse({"message": "Email submitted successfully!"}, status=201)
            else:
                return JsonResponse({"message": "Email already exists!"}, status=400)
        else:
            return JsonResponse({"message": "Invalid email!"}, status=400)
    return JsonResponse({"message": "Method not allowed"}, status=405)
