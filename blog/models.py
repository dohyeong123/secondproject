from django.db import models
from django.utils.timezone import now
# Create your models here.

class Twice(models.Model):
    NATION_CHOICES=(
        ('KR','한국'),
        ('JP','일본'),
        ('TW','대만'),

    )
    name = models.CharField(max_length = 200)
    age = models.IntegerField(default = 0)
    birth= models.DateTimeField(default=now)
    nationality = models.CharField(choices = NATION_CHOICES, max_length = 20)
    position = models.TextField()

    def __str__(self):
        return self.name