from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('searchRecord/', views.searchRecord, name='searchRecord'),
]
