from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def welcome(request):
    mDict = {
        'success': True,
        'message': 'Welcome'
    }
    return JsonResponse(mDict, status=202)
