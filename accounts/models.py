from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User)
	img = models.ImageField(upload_to="imagenes", blank=True, null=True)
	#followers = models.ManyToManyField(User, related_name='followers')

class Contact(models.Model):
	user_from = models.ForeignKey(User, related_name="rel_from_set")
	user_to = models.ForeignKey(User, related_name="rel_to_set")
	created = models.DateTimeField(auto_now_add=True, db_index=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return '{} sigue a {}'. format(self.user_from, self.user_to)

User.add_to_class('following', 
	models.ManyToManyField('self', 
	through=Contact,
	related_name="followers",
	symmetrical=False,))