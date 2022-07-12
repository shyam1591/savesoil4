from django.http import HttpResponse


def index(request):
    """function to return Http response"""
    return HttpResponse('Hello world!')
