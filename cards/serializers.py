from rest_framework import serializers
from cards.models import Card, CardRequest


class CardSerializer(serializers.ModelSerializer):
    member = serializers.StringRelatedField()
    group = serializers.StringRelatedField()
    version = serializers.StringRelatedField()
    type = serializers.StringRelatedField()

    class Meta:
        model = Card
        fields = ('member', 'group', 'version', 'type',)


class CardRequestSerializer(serializers.ModelSerializer):
    requester = serializers.PrimaryKeyRelatedField(read_only=True)
    matcher = serializers.PrimaryKeyRelatedField(read_only=True)
    have_card = serializers.StringRelatedField()

    class Meta:
        model = CardRequest
        fields = ('requester', 'matcher', 'have_card')
