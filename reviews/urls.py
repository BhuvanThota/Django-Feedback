from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name = "reviews"),
    path("thank_you", views.ThankYouView.as_view(), name= "thank_you"),
]