from django.shortcuts import render 

def login(request):
    nombre="Futuro Tecnologico"
    context={
        'nombres':nombre
    }
    return render(request,'index.html',context)

def productos(request):
    titulo="Productos"
    context={
        'titulo':titulo
    }
    return render(request,'productos.html',context)
