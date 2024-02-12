from django.contrib import admin
from django.urls import path
from core import views as core_views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', core_views.home_view, name='home'),
    path('dashboard/', core_views.dashboard_view, name='dashboard'),
    path('update_account/', core_views.update_account_view, name='update_account'),
)
