from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from utils.response_helpers import SuccessResponse, ErrorResponse
from .models import Business, Review, BusinessRegisterStage

class HealthCheck(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        return SuccessResponse(200, message="Server is running")
    
class BusinessRegisterStageAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        try:
            url = request.data.get('url', None)
            if not url:
                return ErrorResponse(400, message="url is required")
            BusinessRegisterStage.objects.create(url=url)
            return SuccessResponse(201, message="BusinessRegisterStage created successfully")
        except Exception as e:
            return ErrorResponse(500, message=str(e))
