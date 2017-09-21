from rest_framework import viewsets
from cards.serializers import CardSerializer, CardRequestSerializer
from cards.models import Card, CardRequest
from django.db.models import Q


class CardsViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    filter_fields = ('group',)


class CardRequestsViewSet(viewsets.ModelViewSet):
    queryset = CardRequest.objects.all()
    serializer_class = CardRequestSerializer

    def get_queryset(self):
        user = self.request.user
        return CardRequest.objects.filter(Q(requester=user) | Q(matcher=user))
