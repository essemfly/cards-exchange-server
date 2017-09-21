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
        fields = ('member', 'group', 'version', 'type',)


class CardRequestSerializer(serializers.ModelSerializer):
    requester = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    matcher = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    have_card = serializers.StringRelatedField()
    want_card = serializers.StringRelatedField()

    class Meta:
        model = CardRequest
        fields = ('requester', 'matcher', 'have_card', 'want_card',
                  'created_date', 'updated_date', 'matched_date', 'status')
