from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    """
    :param request:
    :return: returns rendered html template with welcome message including an username if the user is logged in
             and if not so returns rendered html asking user to register or log in
             and if any exception raises returns an internal server error with the error
    """
    try:
        return render(request,'accounts/index.html')
    except Exception as e:
        return HttpResponse(e, status=500)
