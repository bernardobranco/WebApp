from django.urls import path
from . import views

from django.urls import include

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    #path('set/<uuid:pk>/new/', views.add_new_set, name='add-new-set'),
    path('set/new/', views.add_new_set, name='add-new-set'),
    path('rider/new/', views.add_new_rider, name='add-new-rider'),
]