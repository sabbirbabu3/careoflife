from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
router = DefaultRouter()
router.register('patient', views.PatientViewset)



urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRagistrationAPIviewset.as_view(), name='register'),
    path('active/<uid64>/<token>/', views.activate , name='activate'),
    path('login/', views.UserloginApiView.as_view() , name='login'),
    path('logout/', views.UserlogoutView.as_view() , name='logout'),
]