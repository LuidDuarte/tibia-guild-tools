from django.contrib import messages

def update_player_guild_membership(modeladmin, request, queryset):
    from player.models import Player
    for player in queryset.all():
        try:
            player.update_guild_membership()
            
        except Exception as e:
            msg = f'{player.id}: {e}'
            modeladmin.message_user(request, msg, messages.ERROR)


update_player_guild_membership.short_description = "Update player guild membership"