from django.shortcuts import render, redirect as shortcuts

def inicio(request):
    context={

    }
    return render(request,'index2.html',context)    