from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    test_dict = {'testTemplateTag':'Sou uma template tag!'}
    return render(request, 'alunosApp/index.html', context=test_dict)