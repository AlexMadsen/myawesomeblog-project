from django.db import models

# Create your models here.
class Event(models.Model):
	event_image = models.ImageField(upload_to='event_images/')
	
	