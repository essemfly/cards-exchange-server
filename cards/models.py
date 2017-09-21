from django.db import models
from django.contrib.auth.models import User


class CardGroup(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class CardMember(models.Model):
    name = models.CharField(max_length=50, null=False)
    gender = models.IntegerField(null=0)
    group = models.ForeignKey(CardGroup, on_delete=models.CASCADE)
    birthday = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class CardType(models.Model):
    name = models.CharField(max_length=100, null=False)
    group = models.ForeignKey(CardGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CardVersion(models.Model):
    name = models.CharField(max_length=100, null=False)
    group = models.ForeignKey(CardGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Card(models.Model):
    group = models.ForeignKey(CardGroup, on_delete=models.CASCADE)
    version = models.ForeignKey(CardVersion)
    member = models.ForeignKey(CardMember)
    type = models.ForeignKey(CardType)

    def __str__(self):
        return '%s - %s - %s -%s' % (self.group, self.member, self.version, self.type)


class CardRequest(models.Model):
    requester = models.ForeignKey(User, unique=False, related_name='request_user')
    matcher = models.ForeignKey(User, related_name='matched_user', null=True, blank=True)
    have_card = models.ForeignKey(Card, related_name='have_card')
    want_card = models.ForeignKey(Card, related_name='want_card')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    matched_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default=1)
