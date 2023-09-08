from django.urls import path

from .views import ProblemView

from rest_framework import routers

router = routers.DefaultRouter()
router.register("", ProblemView)

urlpatterns = [] + router.urls
