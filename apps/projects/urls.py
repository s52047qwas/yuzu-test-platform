from rest_framework.routers import DefaultRouter
from . import views


route = DefaultRouter()
route.register('projects', views.ProjectViewSet)
route.register('environment', views.EnvironmentViewSet)

urlpatterns = route.urls
