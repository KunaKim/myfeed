from django.urls import path
from . import views
urlpatterns = [
    # 만든 레지스터 등록
    path('register/', views.register),
    path('login/', views.login),
]
