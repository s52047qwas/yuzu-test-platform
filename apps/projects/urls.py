from rest_framework.routers import DefaultRouter
from . import views


route = DefaultRouter()
route.register('projects', views.ProjectViewSet)
route.register('environment', views.EnvironmentViewSet)
route.register('modules', views.ModuleViewSet)
route.register('interface', views.InterfaceViewSet)


urlpatterns = route.urls
