from django.urls import path

from . import views

# Mes urls qui permettent d'accéder à mes différentes pages
 
urlpatterns = [
   path('index/', views.index, name="index"),
   path('show/<ID_Train>', views.show, name="show"),
]
