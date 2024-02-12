from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from core import htmx_views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', core_views.home_view, name='home'),
    path('dashboard/', core_views.dashboard_view, name='dashboard'),
    path('update_account/', core_views.update_account_view, name='update_account'),
    # htmx
    path('settings_modal_account/', htmx_views.settings_modal_account, name='settings_modal_account'),
    path('settings_modal_password/', htmx_views.settings_modal_password, name='settings_modal_password')
)