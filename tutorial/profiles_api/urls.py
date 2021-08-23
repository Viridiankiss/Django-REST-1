from django.urls import include, path
from profiles_api import views


urlpatterns = [
    path('hello-view/', views.helloApiView.as_view()),
]
