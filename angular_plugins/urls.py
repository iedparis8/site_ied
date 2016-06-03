from django.conf.urls import url, include
from rest_framework import routers
from angular_plugins import views


router = routers.DefaultRouter()
router.register(r'rules', views.RulesViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
