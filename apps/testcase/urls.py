from rest_framework.routers import DefaultRouter
from . import views


route = DefaultRouter()
route.register('task', views.TaskViewSet)
route.register('test_suit', views.TestSuitViewSet)


urlpatterns = route.urls