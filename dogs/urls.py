from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from dogs.views import DogsRegisterView
from dogs.api import DogsImageRegister, DogsImageResponse, DogsKeyboard

urlpatterns = [
    url(r'^images', DogsImageRegister.as_view()),
    url(r'^register', DogsRegisterView.as_view()),
    url(r'^message', DogsImageResponse.as_view()),
    url(r'^keyboard', DogsKeyboard.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
