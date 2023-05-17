from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class News(models.Model):
	headlines = models.CharField(max_length=50)
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	datetime=models.DateTimeField(default=timezone.now)
	content=models.TextField()

	def get_absolute_url(self):
		return reverse("post-detail", kwargs={'pk': self.id})
