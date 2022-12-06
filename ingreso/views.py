from django.shortcuts import render

# Create your views here.
def ingreso(request):
    context={

    }
    return render(request,'ingreso/ingreso.html',context)