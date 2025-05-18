from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet, FragmentViewSet, ResultViewSet
from .auth import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views_session import StartSessionView, SubmitSessionView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'fragments', FragmentViewSet)
router.register(r'results', ResultViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

urlpatterns += [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += [
    path('session/start/', StartSessionView.as_view(), name='start_session'),
    path('session/submit/', SubmitSessionView.as_view(), name='submit_session'),
]
