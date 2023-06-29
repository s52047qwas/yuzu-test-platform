from rest_framework.routers import DefaultRouter
from . import views


route = DefaultRouter()
route.register('task', views.TaskViewSet)
route.register('test_suit', views.TestSuitViewSet)
route.register('testcase', views.TestCaseViewSet)


urlpatterns = route.urls