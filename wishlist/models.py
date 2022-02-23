from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	follows = models.ManyToManyField(
		"self",
		related_name="followed_by",
		symmetrical=False,
		blank=True
		)

	def __str__(self):
		return self.user.username


class Wish(models.Model):
	user = models.ForeignKey(User, related_name="wishes", on_delete=models.DO_NOTHING)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=400, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	url = models.URLField(blank=True)
	picture = models.URLField(blank=True)
	price = models.FloatField(null=True, default=None, blank=True)
	has_commitment = models.BooleanField(default=False)

	def __str__(self):
		return f"\"{self.title}\" by {self.user}"


class Commitment(models.Model):
	user = models.ForeignKey(User, related_name="commitments", on_delete=models.DO_NOTHING)
	wish = models.ForeignKey(Wish, on_delete=models.DO_NOTHING)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"[{self.user}] => [{self.wish}]"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		user_profile = Profile(user=instance)
		user_profile.save()
		user_profile.follows.add(user_profile.id)
		user_profile.save()
