from django.db import models

# Create your models here.

class Post(models.Model):
	date = models.DateTimeField()
	title = models.CharField(max_length=300)
	text = models.TextField()
	image = models.ImageField(upload_to='event_images/')