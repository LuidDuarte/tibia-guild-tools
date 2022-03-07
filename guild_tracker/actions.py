from django.contrib import messages
from .utils import all_players

def update_player_list(modeladmin, request, queryset):
    from player.models import Player
    for guild in queryset.all():
        try:
            #First force update names in case of name_changes avoiding duplicity
            for player in Player.objects.filter(lists__guild=guild):
                player.update_name_if_changed()
            for player in all_players(guild.name):
                if not Player.objects.filter(name=player['name']).exists():
                    Player.objects.create(name=player['name'])
        except Exception as e:
            msg = f'{guild.id}: {e}'
            modeladmin.message_user(request, msg, messages.ERROR)


update_player_list.short_description = "Update player list"