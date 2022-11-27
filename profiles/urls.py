from django.urls import path

from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path("register/", views.register_view, name="register_view"),
    path("login/", views.login_view, name="login_view"),
    path('logout/', views.logout_view, name='logout_view'),

    # Profile
    path('profile/', views.profile_view, name='profile_view'),

    # Password Reset
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='profile/password-reset.html'), name='password_reset_view'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='profile/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='profile/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='profile/password_reset_complete.html'), name='password_reset_complete'),
]
