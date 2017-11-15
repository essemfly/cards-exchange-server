from rest_framework import serializers
from cards.models import Card, CardRequest
from django.contrib.auth.models import User
from datetime import datetime


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
    matcher = serializers.SlugRelatedField(read_only=True, required=False,
                                           slug_field='email')
    have_card = CardSerializer(read_only=True)
    want_card = CardSerializer(read_only=True)
    have_card_id = serializers.PrimaryKeyRelatedField(queryset=Card.objects.all(), source='have_card', write_only=True)
    want_card_id = serializers.PrimaryKeyRelatedField(queryset=Card.objects.all(), source='want_card', write_only=True)

    class Meta:
        model = CardRequest
        fields = ('id', 'requester', 'matcher', 'have_card', 'want_card',
                  'created_date', 'updated_date', 'matched_date', 'status', 'want_card_id', 'have_card_id')

    def create(self, validated_data):
        matched_request = CardRequest.objects.filter(status=1) \
            .filter(want_card=validated_data['have_card']) \
            .filter(have_card=validated_data['want_card']) \
            .order_by('updated_date').first()
        if matched_request:
            matched_time = datetime.now()
            card_request = CardRequest.objects.create(
                requester=self.context['request'].user,
                have_card=validated_data['have_card'],
                want_card=validated_data['want_card'],
                matcher=matched_request.matcher,
                matched_date=matched_time,
                status=2,
            )

            matched_request.matcher = self.context['request'].user
            matched_request.matched_date = matched_time
            matched_request.updated_date = matched_time
            matched_request.status = 2
            matched_request.save()
            return card_request

        else:
            card_request = CardRequest.objects.create(
                requester=self.context['request'].user,
                have_card=validated_data['have_card'],
                want_card=validated_data['want_card']
            )
            return card_request
