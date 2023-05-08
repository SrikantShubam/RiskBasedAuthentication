from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin
from authen import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', csrf_exempt(auth_views.LoginView.as_view(template_name='auth/login.html')), name='login'),
    path('logout/', csrf_exempt(auth_views.LogoutView.as_view()), name='logout'),
    path('signup/', csrf_exempt(views.signup), name='signup'),
    path('admin/', admin.site.urls),
]
