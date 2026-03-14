from django.db import models

# Allow us to extract the EntityUser by default created at the begining
from django.contrib.auth.models import AbstractUser

# We are creating our models for the database using two aprox:
    # Inhereting the entities and attributes created before with commands:
        # pip install psycopg2
        # py managae.py migrate

    # Manually creation, similar as full_name
class User(AbstractUser):
    full_name = models.CharField(max_length=255)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(blank=True, null=True)

