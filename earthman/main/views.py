from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class MainView(View):
    def get(self, request, *args, **kwargs):
        html = '<h1>Coming soon  </h1> ' \
               '<i> <p> Created by P.Mikhailov </p> </i> '
        return HttpResponse(html)
