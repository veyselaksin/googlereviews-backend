from rest_framework import serializers
from .models import Business, Review 

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'
    
        def create(self, validated_data):
            return Business.objects.create(**validated_data)
        
        def update(self, instance, validated_data):
            instance.google_id = validated_data.get('google_id', instance.google_id)
            instance.place_id = validated_data.get('place_id', instance.place_id)
            instance.name = validated_data.get('name', instance.name)
            instance.address = validated_data.get('address', instance.address)
            instance.phone = validated_data.get('phone', instance.phone)
            instance.rating = validated_data.get('rating', instance.rating)
            instance.save()
            return instance

        def delete(self, instance):
            instance.delete()
        
        def get(self, instance):
            return instance

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

        def create(self, validated_data):
            return Review.objects.create(**validated_data)
        
        def update(self, instance, validated_data):
            instance.google_id = validated_data.get('google_id', instance.google_id)
            instance.author_name = validated_data.get('author_name', instance.author_name)
            instance.rating = validated_data.get('rating', instance.rating)
            instance.text = validated_data.get('text', instance.text)
            instance.likes = validated_data.get('likes', instance.likes)
            instance.save()
            return instance
        
        def delete(self, instance):
            instance.delete()

        def get(self, instance):
            return instance