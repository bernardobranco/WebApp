from django.urls import path
from . import views

from django.urls import include

urlpatterns = [
    path('', views.menu, name='menu'),
]

urlpatterns += [
    #path('set/<uuid:pk>/new/', views.add_new_set, name='add-new-set'),
    # path('menu/', views.menu, name='menu'),
    path('set/new/', views.add_new_set, name='add-new-set'),
    path('rider/new/', views.add_new_rider, name='add-new-rider'),
    path('stats/', views.stats, name='stats'),
]