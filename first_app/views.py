from django.shortcuts import render, redirect
from .models import Student, Dojo
from django.contrib import messages

# Create your views here.
def index(request):
    Dojo.objects.first().test()
    context = {
        'all_dojos': Dojo.objects.all(),
        'all_students': Student.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        response_from_models = Dojo.objects.validate(request.POST)
        if len(response_from_models) < 1:
            # passed the validations
            # create the dojo
            Dojo.objects.create(name = request.POST['name'])
        else:
            # send error message to the client
            for error in response_from_models:
                messages.error(request, error)
    return redirect('/')