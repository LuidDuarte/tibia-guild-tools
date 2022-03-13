from django.contrib import admin
from .models import Player
from .actions import update_player_guild_membership




@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    readonly_fields = ('modified', )
    list_display = ('name', 'member_of')
    filter_horizontal = ('common_hunts', )
    actions = [update_player_guild_membership]
