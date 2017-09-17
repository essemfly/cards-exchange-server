from django.db import models
from django.contrib.auth.models import User


class CardGroup(models.Model):
    name = models.CharField(max_length=100, null=False)


class CardMember(models.Model):
    name = models.CharField(max_length=50, null=False)
    gender = models.IntegerField(null=0)
    group = models.ForeignKey(CardGroup, on_delete=models.CASCADE)
    birthday = models.DateTimeField(null=True, blank=True)


class CardType(models.Model):
    name = models.CharField(max_length=100, null=False)
    group = models.ForeignKey(CardGroup, on_delete=models.CASCADE)


class CardVersion(models.Model):
    name = models.CharField(max_length=100, null=False)
    group = models.ForeignKey(CardGroup, on_delete=models.CASCADE)


class Card(models.Model):
    group = models.ForeignKey(CardGroup, on_delete=models.CASCADE)
    version = models.ForeignKey(CardVersion)
    member = models.ForeignKey(CardMember)
    type = models.ForeignKey(CardType)


class CardRequest(models.Model):
    requester_id = models.ForeignKey(User, unique=False)
    requested_card = models.ForeignKey(Card, related_name='have_card')
    matched_card = models.ForeignKey(Card, null=True, related_name='want_card')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    matched_date = models.DateTimeField(null=True, blank=True)
