from django.shortcuts import render
from django.http import HttpResponse
from .forms import employeeApplicationForm


# Create your views here.
# TEST CONNECTION
def index(request):
    return HttpResponse('forms in progress')

# RENDERS FORM ON INDEX.HTML
def appForm(request):
    newForm = employeeApplicationForm()

    context = {
        'newForm': newForm
    }

    return render(request, 'formCWapp/index.html', context)

# GRABS POST AND SENDS TO FORMINFO.HTML
def formInfo(request):
    if (request.method == 'POST'):
        print(request.POST)
        context = {'name': request.POST['name'], 'DOB': request.POST['date_of_birth'],
                   'position': request.POST['position_applying_to'], 'salary': request.POST['salary']}
        return render(request, 'formCWapp/formInfo.html', context)
    else:
        newForm = employeeApplicationForm()

        context = {
            'newForm': newForm
        }

        return render(request, 'formCWapp/index.html', context)
