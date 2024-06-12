from django.urls import path
from .views import home, ChatbotResponseView, chatbot

urlpatterns = [
    path("", home, name='home'),
    path('chatbot/', ChatbotResponseView.as_view(), name='chatbot_response'),
    # path('chat/', chatbot, name='chatbot'),
]
