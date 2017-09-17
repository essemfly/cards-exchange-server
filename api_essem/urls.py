"""api_essem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
from allauth.account.views import confirm_email as allauthemailconfirmation


schema_view = get_swagger_view(title='Essem API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^', include('rest_auth.urls')),
    url(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$',
                      allauthemailconfirmation, name="account_confirm_email"),
    url(r'^registration/', include('rest_auth.registration.urls')),
    url(r'^dogs/', include('dogs.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
