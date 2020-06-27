from rest_framework import serializers
from .models import Bootcamp, User, Course, Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'],
                    email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class BootcampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bootcamp
        fields = ('id', 'publisher', 'courses', 'name', 'description', 'address',
                  'zipcode', 'website', 'phone', 'email', 'careers', 'housing',
                  'jobAssistance', 'jobGuarantee', 'acceptGi')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'weeks', 'tuition', 'minimumSkill',
                  'scholarhipsAvailable',)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'forWhichBootcamp', 'title', 'text', 'rating',)
