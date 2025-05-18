import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Fragment, Result
from .serializers import ResultSerializer
from django.utils import timezone


class StartSessionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        fragments = Fragment.objects.all()
        if not fragments.exists():
            return Response({"error": "No fragments available"}, status=404)

        fragment = random.choice(fragments)
        return Response({
            "fragment_id": fragment.id,
            "content": fragment.content,
            "complexity": fragment.complexity_level,
            "theme": fragment.theme,
        })


class SubmitSessionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data

        try:
            fragment = Fragment.objects.get(id=data['fragment_id'])
        except Fragment.DoesNotExist:
            return Response({"error": "Fragment not found"}, status=404)

        # Пример простейшего расчёта скорости (можно усложнить позже)
        word_count = len(fragment.content.split())
        time_minutes = data.get("time_seconds", 60) / 60
        reading_speed = round(word_count / time_minutes)

        # Простая формула понимания (в будущем подключим ИИ)
        comprehension = data.get("comprehension", 0)

        result = Result.objects.create(
            user=request.user,
            fragment=fragment,
            reading_speed=reading_speed,
            comprehension=comprehension,
            session_data=data.get("session_data", {}),
            test_date=timezone.now()
        )

        return Response(ResultSerializer(result).data, status=status.HTTP_201_CREATED)
