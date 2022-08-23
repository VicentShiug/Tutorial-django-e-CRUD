from django.urls import path

from lista.views import delete, index, indexdetails, add, update

urlpatterns = [
    path('index/', index, name='index'),
    path('details/<int:id>', indexdetails, name='details'),
    path('add/', add, name='add'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
]