from django.contrib import admin
from .models import Player
from guild_tracker.admin import PlayerListInline


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    readonly_fields = ('modified', )
