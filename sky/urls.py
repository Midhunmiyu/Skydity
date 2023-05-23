from django.urls import path

from sky import views

urlpatterns = [
    path('', views.index,name='index'),
]
