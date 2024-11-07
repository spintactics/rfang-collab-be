from django.urls import path
from .views import DocumentCreateView, LoginView, LogoutView, SignupView

urlpatterns = [
    path('documents/', DocumentCreateView.as_view(), name='create_document'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
]
