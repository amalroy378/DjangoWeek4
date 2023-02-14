import re
from django.conf import settings
from django.shortcuts import redirect



class LoginRequiredMiddleware:
    def __init__(self,get_response):
        self.get_reponse=get_response

    def __call__(self,request):

        response= self.get_reponse(request)
        return response


        