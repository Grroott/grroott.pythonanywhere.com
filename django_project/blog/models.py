from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MinLengthValidator

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(validators=[MinLengthValidator(200)])
	liked = models.ManyToManyField(User, default=None, blank=True, related_name = 'liked')
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'author')

	def __str__(self):
		return self.title

	@property
	def num_likes(self):
		return self.liked.all().count()

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

LIKE_CHOICES = (

('Like', 'Like'),
('Unlike', 'Unlike'),

)

class Like(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	value = models.CharField(choices= LIKE_CHOICES,default='Like', max_length=10)


	def __str__(self):
		return str(self.post)
