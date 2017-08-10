from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from dogs.views import DogsRegisterView
from dogs.api import DogsImageRegister

urlpatterns = [
    url(r'^images', DogsImageRegister.as_view()),
    url(r'^register', DogsRegisterView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
