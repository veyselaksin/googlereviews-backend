from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from utils.response_helpers import SuccessResponse, ErrorResponse
from .models import Business, Review, BusinessRegisterStage
import os
from outscraper import ApiClient
from .serializers import BusinessSerializer, ReviewSerializer

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
        except Exception:
            return ErrorResponse(500, message="Unexpected error occured")

class BusinessAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        try:
            businesses = Business.objects.all()
            response = BusinessSerializer(businesses, many=True)
            return SuccessResponse(200, message="Businesses retrieved successfully", data=response.data)
        except Exception:
            return ErrorResponse(500, message="Unexpected error occured")

class ReviewAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk, format=None):
        try:
            reviews = Review.objects.filter(google_id=pk)
            response = ReviewSerializer(reviews, many=True)
            return SuccessResponse(200, message="Reviews retrieved successfully", data=response.data)
        except Exception:
            return ErrorResponse(500, message="Unexpected error occured")

# TODO: This is a cron job, it should be moved to a separate file
class CronJob(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        try:
            # get an instance of BusinessRegisterStage
            business_register_stage = BusinessRegisterStage.objects.get(id=1)
            client = ApiClient(api_key=os.environ.get('OUTSCRAPER_API_KEY'))
            # reviews limit unlimited
            result = client.google_maps_business_reviews(business_register_stage.url, reviews_limit=0, sort='newest')

            # create a business instance
            business = Business.objects.create(
                google_id=result[0]['google_id'],
                place_id=result[0]['place_id'],
                name=result[0]['name'],
                address=result[0]['full_address'],
                phone=result[0]['phone'],
                rating=result[0]['rating']
            ).save()

            # create reviews instances
            for review in result[0]['reviews_data']:
                if review['review_text'] == None:
                    review['review_text'] = ""
                Review.objects.create(
                    google_id=review['google_id'],
                    author_name=review['author_title'],
                    rating=review['review_rating'],
                    text=review['review_text'],
                    likes=review['review_likes'],
                ).save()

            return SuccessResponse(200, message="CronJob executed successfully", data=result)
        except Exception as err:
            print("Unexpected error:", err)
            return ErrorResponse(500, message="Unexpected error occured")