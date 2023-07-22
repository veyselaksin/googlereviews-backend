from django.urls import path
from .api import (
    BusinessRegisterStageAPI, HealthCheck,
    BusinessAPI, ReviewAPI, CronJob
)

urlpatterns = [
    path("health-check/", HealthCheck.as_view(), name="health-check"),
    path("register-stage/", BusinessRegisterStageAPI.as_view(), name="register-stage"),
    path("business/", BusinessAPI.as_view(), name="business"),
    path("review/<str:pk>/", ReviewAPI.as_view(), name="review"),
    path("cron-job/", CronJob.as_view(), name="cron-job"),
]

