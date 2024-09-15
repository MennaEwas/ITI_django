from django.urls import path
from . import views
# from .views import cbv

#link project urls to app urls (done in project/urls)
#route patterns with views of mart 
urlpatterns = [
    path('', views.index, name = "index"),
    path('show', views.show, name="show"),
    # path('cbv', cbv.as_view(), name = "cbv"),
]