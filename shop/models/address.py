from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    DEPARTAMENT_CHOICES = [
        ('LP', 'La Paz'),
        ('CB', 'Cochabamba'),
        ('SC', 'Santa Cruz'),
        ('OR', 'Oruro'),
        ('PT', 'Potosí'),
        ('CH', 'Chuquisaca'),
        ('TJ', 'Tarija'),
        ('BN', 'Beni'),
        ('PD', 'Pando'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    departament = models.CharField(max_length=2, choices=DEPARTAMENT_CHOICES)
    country = models.CharField(max_length=100, default='Bolivia')

    def __str__(self):
        return f"{self.user.username}'s address"