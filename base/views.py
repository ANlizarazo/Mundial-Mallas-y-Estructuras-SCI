from django.shortcuts import render, redirect as shortcuts

def inicioAdmin(request):
    context={

    }
    return render(request,'index.html',context)