from django.urls import path
from .views import home, ChatbotResponseView

urlpatterns = [
    path("", home, name='home'),
    path("chatbot/", ChatbotResponseView.as_view(), name='chatbot'),
]
