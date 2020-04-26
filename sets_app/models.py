from django.db import models

from django.urls import reverse

# Create your models here.

class Rider(models.Model):
    """Model representing a rider"""
    first_name = models.CharField(verbose_name="First name", max_length=100)
    last_name = models.CharField(verbose_name="Last name", max_length=100)
    nationality = models.CharField(verbose_name="Nationality", max_length=100)
    date_of_birth = models.DateField(verbose_name="Birth date")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Boat(models.Model):
    """Model representing a boat"""

    brand = models.TextField(verbose_name="Brand of boat")
    model = models.TextField(verbose_name="Model of boat")
    date_added = models.DateField(verbose_name="Date boat was added to fleet")

    def __str__(self):
        return f"{self.brand} {self.model}"


class Set(models.Model):
    """Class defining set entry model"""

    date_time_entry = models.DateTimeField(
        verbose_name="DateTime of entry", auto_now_add=True
    )
    date_set = models.DateField(verbose_name="Date of set")
    duration = models.FloatField(verbose_name="Duration of set")
    driver = models.TextField(verbose_name="Name of driver")
    rider = models.ForeignKey(Rider, help_text="Select boat used for set", on_delete=models.SET_NULL, null=True)
    boat = models.ForeignKey(Boat, help_text="Select boat used for set", on_delete=models.SET_NULL, null=True)

    # Metadataoat
    class Meta:
        ordering = ['-date_set', 'boat']

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return f"Day: {self.date_set} | Driver: {self.driver} | Rider: {self.rider} | Duration: {self.duration}min | Boat: {self.boat}"
