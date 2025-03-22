from django.urls import path
from .views import save_chat_id

urlpatterns = [
    path("api/save_chat_id/", save_chat_id, name="save_chat_id"),
]
