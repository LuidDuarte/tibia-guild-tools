from django.contrib import admin
from .models import Guild, PlayerList
from .actions import update_player_list


class PlayerListInline(admin.TabularInline):
    model = PlayerList
    extra = 0
    filter_horizontal = ('players',)
    exclude = ('id', 'modified',  )


@admin.register(Guild)
class GuildAdmin(admin.ModelAdmin):
    inlines = (PlayerListInline, )
    readonly_fields = ('modified', )
    actions = [update_player_list]
