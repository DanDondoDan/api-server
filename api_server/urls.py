"""api_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from api_server.routers import router
from api_server import views
from api_server import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    url('^api/', include(router.urls)),
    url(r'^department/(?P<pk>[0-9]+)/employeers/$', views.DepartmentEmployeerView.as_view()),
    path('person/<int:pk>/', views.PersonDetailView.as_view(), name="employee-detail"),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name="product-detail"),

    path('exchange/', views.ExchangeViewSet.as_view(), name="exchange"),
    
    url(r'^sign-up/', views.CustomUser.as_view()),
    url(r'rest-auth/', include('rest_auth.urls')),

    
    url(r'^rest-auth/login/', views.LoginView.as_view(), name='rest_login'),
    url('google/login/', views.GoogleLoginView.as_view(), name='google_login'),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# https://www.slideshare.net/kranonit/kranonits20
# https://toster.ru/q/232782
# https://github.com/awesto/django-shop