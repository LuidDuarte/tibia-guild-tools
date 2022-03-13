from django.db import models
from behaviors.behaviors import Timestamped
import uuid


class HuntingGround(Timestamped):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Exiva(Timestamped):
    DISTANCE_CHOICES = (
        ("F", "Far"),
        ("VF", "Very-Far"),
        ("N", " ")
    )
    DIRECTION_CHOICES = (
        ("N", "North"),
        ("W", "West"),
        ("E", "East"),
        ("S", "South"),
        ("NW", "North-West"),
        ("NE", "North-East"),
        ("SE", "South-East"),
        ("SW", "South-West")
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    reference = models.CharField(max_length=35)
    distance = models.CharField(max_length=2, choices=DISTANCE_CHOICES, blank=False, null=False)
    direction = models.CharField(max_length=2, choices=DIRECTION_CHOICES, blank=False, null=False)

    def __str__(self):
        return f'{self.get_distance_display()} {self.get_direction_display()} from {self.reference}'



class HuntingExiva(Timestamped):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    exiva = models.ForeignKey(Exiva, on_delete=models.CASCADE, related_name='hunting_exiva')
    hunt = models.ForeignKey(HuntingGround, on_delete=models.CASCADE, related_name='hunting_exiva')
    priority = models.PositiveSmallIntegerField(help_text='0 is highest priority')

    def __str__(self):
        return f'{self.exiva} - {self.hunt}'