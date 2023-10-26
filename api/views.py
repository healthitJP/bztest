from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from datetime import datetime

def get_local_time(request):
    current_time = datetime.now()
    return JsonResponse({'local_time': current_time.strftime('%Y-%m-%d %H:%M:%S')})

