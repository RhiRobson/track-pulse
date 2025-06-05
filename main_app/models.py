from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Run(models.Model):
    name = models.CharField(max_length=100)
    distance = models.FloatField(help_text="Distance in kilometers")
    time = models.DurationField(help_text="Time duration (hh:mm)")
    notes = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.distance} km"

    def get_absolute_url(self):
        return reverse('run-detail', kwargs={'run_id': self.id})

