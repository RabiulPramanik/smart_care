from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('list', views.DoctorViewsets)
router.register('designations', views.DesignationViewsets)
router.register('specializations', views.SpecializationViewsets)
router.register('reviews', views.ReviewViewsets)
router.register('availabletimes', views.AvailableTimeViewsets)

urlpatterns = [
    path('', include(router.urls)),
]