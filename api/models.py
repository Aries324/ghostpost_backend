from django.db import models
from django.utils.timezone import now
# https://stackoverflow.com/questions/2771676/django-datetime-issues-default-datetime-now#2771701


# Create your models here.


class Posts_Review(models.Model):
    is_boast = models.BooleanField(default=True)
    content = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.is_boast:
            return 'Boast'
        else:
            return 'Roast'

