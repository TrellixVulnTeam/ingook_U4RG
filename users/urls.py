from django.urls import path
from users import views

urlpatterns = [
    path('users/', views.user_list),
    path('user/<str:login_id>/<str:login_pw>', views.user)
]