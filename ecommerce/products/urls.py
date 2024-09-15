from django.urls import path

from . import views

urlpatterns = [
    path('listprod', views.products, name = "products"),

]