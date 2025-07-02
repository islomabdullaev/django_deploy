from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello, World! This is a test deployment and updated !")