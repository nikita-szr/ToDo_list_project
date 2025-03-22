from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    @action(detail=False, methods=['get'])
    def my_tasks(self, request):
        tasks = self.get_queryset()
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


User = get_user_model()


@api_view(["POST"])
def save_chat_id(request):
    user_id = request.data.get("user_id")
    chat_id = request.data.get("chat_id")

    if not user_id or not chat_id:
        return Response({"error": "user_id and chat_id are required"}, status=400)

    try:
        user = User.objects.get(id=user_id)
        user.telegram_chat_id = chat_id
        user.save()
        return Response({"message": "Chat ID saved successfully"})
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
