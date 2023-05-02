from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('product/<int:pk>/', views.detail, name='product_detail'),
    path('signup/', views.signup, name='signup'),
    path('new/', views.new, name='new'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html', authentication_form = LoginForm), name='login'),
    path('/',auth_views.LogoutView.as_view(template_name='index.html'),name="logout"),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
