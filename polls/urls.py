from django.urls import path
from .views import GreetingPageView, DetailQuestion, ResultView

urlpatterns = [
    path('', GreetingPageView.as_view(), name='greeting'),
    path('<int:pk>/', DetailQuestion.as_view(), name='question'),
    path('result/', ResultView.as_view(), name='result')
]