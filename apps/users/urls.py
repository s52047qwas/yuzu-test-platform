from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from . import views
from rest_framework.routers import DefaultRouter

# rest_framework视图集url设置
route = DefaultRouter()
route.register('', views.UserViewSet)

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('token/refresh/', views.RefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('', include(route.urls))
]