from rest_framework import viewsets
from .models import User, Fragment, Result
from .serializers import UserSerializer, FragmentSerializer, ResultSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FragmentViewSet(viewsets.ModelViewSet):
    queryset = Fragment.objects.all()
    serializer_class = FragmentSerializer


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
