from django.db import models
from behaviors.behaviors import Timestamped
import uuid

class Player(Timestamped):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    member_of = models.ForeignKey('guild_tracker.Guild', on_delete=models.SET_NULL, blank=True, null=True)
    common_hunts = models.ManyToManyField('hunting_places.HuntingGround', related_name='players', blank=True, null=True)

    def __str__(self):
        return self.name

    def update_name_if_changed(self):
        from .utils import check_player_name
        player_name_remote = check_player_name(self.name)
        if player_name_remote != self.name:
            self.name = player_name_remote
            self.save()

    def update_guild_membership(self):
        from .utils import check_guild_membership
        from guild_tracker.models import Guild
        guild_name = check_guild_membership(self.name)
        if guild_name != self.guild_name:
            self.member_of = Guild.objects.get(name=guild_name) if guild_name else None
            self.save()
    
    @property
    def guild_name(self):
        return self.member_of.name if self.member_of else None
