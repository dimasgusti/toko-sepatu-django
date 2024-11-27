from django.db import models

class User(models.Model):
    USER = 'user'
    ADMIN = 'admin'
    COURIER = 'courier'
    
    ROLE_CHOICES = [
        (USER, 'User'),
        (ADMIN, 'Admin'),
        (COURIER, 'Courier'),
    ]
    role = models.CharField(
        max_length=7,
        choices=ROLE_CHOICES,
        default=USER
    )
    username = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    password = models.TextField(max_length=64)
    address = models.TextField(max_length=64)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username
