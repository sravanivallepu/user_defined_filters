from django.shortcuts import render

# Create your views here.
def filters(request):
    d={'data':'Hai How ARE yoU'}
    return render(request,'usdfilters.html',d)