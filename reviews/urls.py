from django.urls import path
from .api import BusinessRegisterStageAPI, HealthCheck

urlpatterns = [
    path("health-check/", HealthCheck.as_view(), name="health-check"),
    path("register-stage/", BusinessRegisterStageAPI.as_view(), name="register-stage"),
]

