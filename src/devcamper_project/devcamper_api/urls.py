from rest_framework import routers
from .views import (BootcampsViewSet, UsersViewSet, UpdatePasswordView,
                    CoursesViewSet, CoursesOfBootcamps, ReviewsViewSet,
                    ReviewsOfBootcamps, TokenViewSet)

from django.urls import path, include

router = routers.DefaultRouter()
router.register('bootcamps', BootcampsViewSet)
router.register('users', UsersViewSet)
router.register('courses', CoursesViewSet)
router.register('reviews', ReviewsViewSet)
router.register('token', TokenViewSet, basename='token')

urlpatterns = [
    path('', include(router.urls)),
    path('updatepassword/', UpdatePasswordView.as_view()),
    path('bootcamps/<int:id>/courses/', CoursesOfBootcamps.as_view()),
    path('bootcamps/<int:id>/reviews/', ReviewsOfBootcamps.as_view())
]
