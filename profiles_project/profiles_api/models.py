from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(object):
	"""helps django work with our custom user model"""
	def create_user(self,email,name,password=None):
		if not email:
			raise ValueError('User must have email')
		email = self.normalize_email(email)
		user = self.model(email=email, name=name)

		user.set_password(password)
	
		







class UserProfile(AbstractBaseUser, PermissionMixin):

	"""docstring for UserProfile"""
	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	object = UserProfileManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']

	def get_full_name(self):
		"""used to get a user full name"""
		return self.name

	def get_short_name():
		"""used to get a users short name"""
		return self.name

	def __str__(self):
		"""Django uses this when it needs to convert the object into string"""
		return self.email
		
