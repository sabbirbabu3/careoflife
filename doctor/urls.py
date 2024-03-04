from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
router = DefaultRouter()
router.register('doctor', views.DoctorViewset)
router.register('designation', views.DesignationViewset)
router.register('specialization', views.SpecializationViewset)
router.register('available_time', views.AvailableTimeViewset)
router.register('review', views.ReviewViewset)


urlpatterns = [
    path('', include(router.urls)),
]