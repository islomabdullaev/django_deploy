from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello, World! Runned with self hosted runner")