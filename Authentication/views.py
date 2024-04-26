from django.shortcuts import render # type: ignore
from rest_framework.views import APIView # type: ignore
from django.http import JsonResponse #type: ignore
from rest_framework import permissions



class Login(APIView):
    permission_classes = (permissions.IsAuthenticated,) # type: ignore
    JsonResponse({'Success': 'You are Logged In'}, status=200)
        