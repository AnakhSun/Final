from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet, FragmentViewSet, ResultViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'fragments', FragmentViewSet)
router.register(r'results', ResultViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
