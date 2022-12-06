from django.urls import path
from ingreso.views import ingreso

urlpatterns = [
    path('',ingreso,name="ingreso"),
]