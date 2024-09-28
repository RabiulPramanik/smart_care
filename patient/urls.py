from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('list', views.PatientViewsets)

urlpatterns = [
    path('', include(router.urls)),
    path('registration/', views.RegistrationsView.as_view(), name='registration' ),
    path('login/', views.LoginView.as_view(), name='login' ),
    path('logout/', views.LogoutView.as_view(), name='logout' ),
    path('active/<uid64>/<token>', views.activate, name="activate"),
]