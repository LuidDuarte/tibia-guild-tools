from django.db import models
from behaviors.behaviors import Timestamped
import uuid


class Guild(Timestamped):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True)

    def __str__(self) -> str:
        return self.name

    def online_members(self):
        from .utils import online_players
        return online_players(self.name)

    def sort_by_priority(self):
        from .utils import get_dict_from_array
        lists = [{'name': x.name, 'priority': x.priority, 'online': [], 'default': x.default} for x in self.lists.all()]
        online_members = self.online_members()
        for member in online_members:
            player_in_list = self.lists.filter(players__name__iexact=member.get('name'))
            if player_in_list.exists():
                get_dict_from_array(lists, 'name', player_in_list.name)['online'].append(member)
            else:
                get_dict_from_array(lists, 'default', True)['online'].append(member)
        for list in lists:
            list.update({'online':  sorted(list['online'], key=lambda x : x['level'], reverse=True)})
        return lists





class PlayerList(Timestamped):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE, related_name='lists')
    name = models.CharField(max_length=10, null=False, blank=False)
    players = models.ManyToManyField('player.Player', related_name='lists', blank=True, null=True)
    priority = models.PositiveSmallIntegerField(unique=True, help_text='0 is highest priority')
    default = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.priority}'

    class Meta:
        ordering = ('priority',)
