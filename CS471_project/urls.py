
from django.contrib import admin
from django.urls import include, path
from base import views
from django.views.generic.base import TemplateView

urlpatterns = [
     path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("admin/", admin.site.urls),
    path('', views.show_base, name='show_base'),
    path('', include('base.urls')),
    path('home', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
