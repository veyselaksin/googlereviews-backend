import sys
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.db.models import Q

from ..reviews.models import Business, Review, BusinessRegisterStage

import os
from outscraper import ApiClient

def register_business_handler():
    try:
        # outscraper client
        client = ApiClient(api_key=os.environ.get('OUTSCRAPER_API_KEY'))

        # get instances of BusinessRegisterStage
        business_register_stage = BusinessRegisterStage.objects.all()

        for business in business_register_stage:
            # reviews limit unlimited
            result = client.google_maps_business_reviews(business.url, reviews_limit=0)

            # create a business instance
            Business.objects.create(
                google_id=result[0]['google_id'],
                place_id=result[0]['place_id'],
                name=result[0]['name'],
                address=result[0]['full_address'],
                phone=result[0]['phone'],
                rating=result[0]['rating']
            ).save()

        # # create reviews instances
        # for review in result[0]['reviews_data']:
        #     if review['review_text'] == None:
        #         review['review_text'] = ""
        #     Review.objects.create(
        #         google_id=review['google_id'],
        #         author_name=review['author_title'],
        #         rating=review['review_rating'],
        #         text=review['review_text'],
        #         likes=review['review_likes'],
        #     ).save()

        return True
    except Exception:
        return False