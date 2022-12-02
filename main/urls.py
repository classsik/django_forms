from django.urls import path

from .views import home, appointment, order

urlpatterns = [
    path('', home),
    path('appointment', appointment),
    path('order', order),
]
