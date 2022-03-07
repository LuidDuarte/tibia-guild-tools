from django.db import models
from behaviors.behaviors import Timestamped
import uuid

class Player(Timestamped):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def update_name_if_changed(self):
        from .utils import check_player_name
        player_name_remote = check_player_name(self.name)
        if player_name_remote != self.name:
            self.name = player_name_remote
            self.save()
