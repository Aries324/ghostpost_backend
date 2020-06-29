from django.db import models
# https://stackoverflow.com/questions/2771676/django-datetime-issues-default-datetime-now#2771701


# Create your models here.


class Posts_Review(models.Model):
    is_boast = models.BooleanField(default=True)
    content = models.CharField(max_length=280)
    up_votes = models.PositiveIntegerField(default=0)
    down_votes = models.PositiveIntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.is_boast:
            return 'Boast'
        else:
            return 'Roast'

    def total_votes(self):
        return self.up_votes - self.down_votes



