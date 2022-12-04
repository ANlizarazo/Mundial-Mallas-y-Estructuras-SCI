from django.shortcuts import render 

def holamundo(request):
    context={}
    return(request,'index.html',context)