from django.db import models
from django.urls import reverse

class Run(models.Model):
    name = models.CharField(max_length=100)
    distance = models.FloatField(help_text="Distance in kilometers")
    time = models.DurationField(help_text="Time duration (hh:mm:ss)")
    notes = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.distance} km"

    def get_absolute_url(self):
        return reverse('run-detail', kwargs={'run_id': self.id})
