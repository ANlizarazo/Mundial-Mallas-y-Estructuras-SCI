from django.shortcuts import render 

def login(request):
    nombre="Futuro Tecnologico"
    context={
        'nombres':nombre
    }
    return render(request,'index.html',context)