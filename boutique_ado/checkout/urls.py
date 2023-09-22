from django.urls import path
from . import views

urlpatterns = [
    path("", views.checkoutView, name="checkoutView")
]
