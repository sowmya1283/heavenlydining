from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    displayname = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.displayname


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bookings")
    table_size = models.PositiveIntegerField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    allergies = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['user']
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return (
            f"Booking by {self.user} "
            f"on {self.booking_date} "
            f"at {self.booking_time} "
            f"for {self.table_size} people"
        )
