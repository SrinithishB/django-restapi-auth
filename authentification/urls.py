from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('home/', views.HomeView.as_view(), name ='home'),
    path('logout/', views.LogoutView.as_view(), name ='logout'),
    path('forgotpass/', views.ForgotPasswordView.as_view(), name='forgot-password'),
    path('resetpass/<uidb64>/<token>/', views.ResetPasswordView.as_view(), name='reset-password'),
    path('createuser/', views.CreateUserView.as_view(), name='create-user'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
]