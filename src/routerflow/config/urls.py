from django.contrib import admin
from django.urls import path
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home_view, name='home'),
    path('dashboard/', core_views.dashboard_view, name='dashboard'),
    path('update_account/', core_views.update_account_view, name='update_account'),
]
