from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES = (("CREAMIC", "CREAMIC"), ("GLASS", "GLASS"),
                    ("STAINLESS", "STAINLESS"), ("MELAMINE ", "MELAMINE"), ("CHINA ", "CHINA"))


class Mug(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    quantity = models.IntegerField(null=True, blank=True)
    created_by = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=100)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isSTAFF = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}'
