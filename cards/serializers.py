from rest_framework import serializers
from cards.models import Card, CardRequest
from django.contrib.auth.models import User


class CardSerializer(serializers.ModelSerializer):
    member = serializers.StringRelatedField()
    group = serializers.StringRelatedField()
    version = serializers.StringRelatedField()
    type = serializers.StringRelatedField()

    class Meta:
        model = Card
        fields = ('id', 'member', 'group', 'version', 'type',)


class CardRequestSerializer(serializers.ModelSerializer):
    requester = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    matcher = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    have_card = CardSerializer(read_only=True)
    want_card = CardSerializer(read_only=True)
    have_card_id = serializers.PrimaryKeyRelatedField(queryset=Card.objects.all(), source='have_card', write_only=True)
    want_card_id = serializers.PrimaryKeyRelatedField(queryset=Card.objects.all(), source='want_card', write_only=True)

    class Meta:
        model = CardRequest
        fields = ('id', 'requester', 'matcher', 'have_card', 'want_card',
                  'created_date', 'updated_date', 'matched_date', 'status', 'want_card_id', 'have_card_id')

    def create(self, validated_data):
        card_request = CardRequest.objects.create(
            requester=self.context['request'].user,
            have_card=validated_data['have_card'],
            want_card=validated_data['want_card']
        )
        return card_request
