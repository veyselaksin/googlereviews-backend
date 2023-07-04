from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from utils.response_helpers import SuccessResponse, ErrorResponse

class Reviews(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        return SuccessResponse(200, data="Hello World", message="Hello World")


