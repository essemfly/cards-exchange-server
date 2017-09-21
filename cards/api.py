from rest_framework import viewsets
from cards.serializers import CardSerializer, CardRequestSerializer
from cards.models import Card, CardRequest


class CardsViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    filter_fields = ('group',)


class CardRequestsViewSet(viewsets.ModelViewSet):
    queryset = CardRequest.objects.all()
    serializer_class = CardRequestSerializer