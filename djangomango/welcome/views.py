from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("Seja Bem Vindo!!")
    return render(request, 'view.html')