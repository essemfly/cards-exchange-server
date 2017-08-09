from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from dogs.views import DogsList

urlpatterns = [
    url(r'^', DogsList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
