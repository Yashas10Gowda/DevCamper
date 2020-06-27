from django.shortcuts import render
from .models import Bootcamp, User, Course, Review
from rest_framework import viewsets, filters, views, response, authentication, permissions
from .serializers import BootcampSerializer, UserSerializer, CourseSerializer, ReviewSerializer
from .permissions import UsersPermissions, BootcampsPermissions, CoursesPermissions, ReviewsPermissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken


class TokenViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().post(request)


class UpdatePasswordView(views.APIView):
    def get(self, request):
        return response.Response(
            {"ExpectedRequest": {'username': 'actualUsername', 'password': 'ToBeUpdatedPassword'}})

    def post(self, request):
        print(request.data['password'])
        if request.user.username != request.data['username']:
            return None
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        return response.Response({'Password Changed': True})


class CoursesOfBootcamps(views.APIView):
    def get(self, request, id):
        bootcamp = Bootcamp.objects.get(id=id)
        coursesquery = list(bootcamp.courses.all())
        courses = []
        for course in coursesquery:
            courses.append(course.title)
        return response.Response(
            {f'Courses Offered By {bootcamp.name} are': courses})


class ReviewsOfBootcamps(views.APIView):
    def get(self, request, id):
        bootcamp = Bootcamp.objects.get(id=id)
        reviewsquery = Review.objects.filter(forWhichBootcamp=id)
        reviews = []
        for review in reviewsquery:
            reviews.append({review.title: review.rating})
        return response.Response(
            {f'{bootcamp.name} Bootcamp Reviews': reviews})


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, UsersPermissions,)
    authentication_classes = (authentication.TokenAuthentication,)
    queryset = User.objects.all()


class BootcampsViewSet(viewsets.ModelViewSet):
    serializer_class = BootcampSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, BootcampsPermissions,)
    authentication_classes = (authentication.TokenAuthentication,)
    queryset = Bootcamp.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('zipcode',)


class CoursesViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, CoursesPermissions,)
    authentication_classes = (authentication.TokenAuthentication,)
    queryset = Course.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)


class ReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (ReviewsPermissions,)
    queryset = Review.objects.all()
