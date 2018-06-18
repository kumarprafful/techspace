from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class UserProfile(models.Model):
		
	user = models.OneToOneField(User, on_delete=models.PROTECT)
	club_choice = (
		('nothing', 'nothing'),
		('codeschool', 'codeschool'),
		('cogitans', 'cogitans'),
		('ecell', 'ecell'),
		('electrotech', 'electrotech'),
		('oslc', 'oslc'),
		('renderedusict', 'renderedusict'),
		('turingai', 'turingai'),
		('techspace', 'techspace')
	)

	club = models.CharField(max_length=255, choices=club_choice, default='nothing')

	def __str__(self):
		return self.user.username

