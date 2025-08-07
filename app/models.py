from django.db import models

# Create your models here.
class images_data(models.Model):
      Images = models.FileField(upload_to='Images')