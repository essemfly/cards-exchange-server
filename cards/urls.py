from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from cards.api import CardsViewSet, CardRequestsViewSet

router = DefaultRouter()
router.register(r'cards', CardsViewSet)
router.register(r'requests', CardRequestsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
