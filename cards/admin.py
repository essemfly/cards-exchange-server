from django.contrib import admin
from .models import (
    Card, CardGroup, CardMember, CardType, CardVersion
)


class CardGroupAdmin(admin.ModelAdmin):
    model = CardGroup
    list_display = ['name']


class CardMemberAdmin(admin.ModelAdmin):
    model = CardMember
    list_display = ['name', 'group']


class CardVersionAdmin(admin.ModelAdmin):
    model = CardVersion
    list_display = ['name', 'group']


class CardTypeAdmin(admin.ModelAdmin):
    model = CardType
    list_display = ['name', 'group']


class CardAdmin(admin.ModelAdmin):
    model = Card
    list_display = ['group', 'version', 'member', 'type']


admin.site.register(CardGroup, CardGroupAdmin)
admin.site.register(CardMember, CardMemberAdmin)
admin.site.register(CardVersion, CardVersionAdmin)
admin.site.register(CardType, CardTypeAdmin)
admin.site.register(Card, CardAdmin)
