from django.urls import path
from .api import Reviews

urlpatterns = [
    path("", Reviews.as_view(), name="reviews"),
]

