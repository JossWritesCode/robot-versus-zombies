from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rvz_api import views

router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view())
]
