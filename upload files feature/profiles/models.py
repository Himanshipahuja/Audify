from django.db import models

# Create your models here.


class UserProfile(models.Model):
    image = models.FileField(upload_to="images")

    # def __str__(self):
    #     return self.image
