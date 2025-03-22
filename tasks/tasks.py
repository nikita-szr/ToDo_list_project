from celery import shared_task
from django.utils.timezone import now
from .models import Task
import requests
import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"


@shared_task
def send_task_reminder():
    tasks = Task.objects.filter(due_date__lte=now())
    for task in tasks:
        message = f"🔔 Напоминание!\nВаша задача '{task.title}' должна быть выполнена!"
        send_telegram_message(task.user.telegram_chat_id, message)


def send_telegram_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)