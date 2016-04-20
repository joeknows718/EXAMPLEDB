from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from unique_slug import unique_slugify 
from django.conf import settings
from django.core.mail import send_mail




GENDER_CHOICES = (('M', 'M'),
	('F', 'F'),
	('Not Sure', 'Not Sure'))

BOOL_CHOICES =(('Yes', 'Yes'),
	('No', 'No'),
	('Not Sure', 'Not Sure'))

# Create your models here.

class UserProfile(AbstractUser):
	is_approved = models.BooleanField(default=False)
	organization = models.CharField(blank=True, max_length=144)


@receiver(pre_save, sender=UserProfile, dispatch_uid='approved')
def approved(sender, instance, **kwargs):
	subject = 'You account is approved!'
	message = '%s your account is now approved. You can now, begin to use the Prosecutor DB Project Log In Here: http://prosecutordb.org/login' %(instance.username)
	from_email = settings.EMAIL_HOST_USER
	if instance.is_approved and UserProfile.objects.filter(pk=instance.pk, is_approved=False).exists():
		send_mail(subject, message, from_email, [instance.email], fail_silently=False)




class State(models.Model):
	state_short = models.CharField(blank=False, max_length=3, primary_key=True)
	state_name = models.CharField(blank=False, max_length=100)
	notes = models.TextField(blank=True)
	slug = models.SlugField(blank=True, null=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.state_name)
		super(State, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.state_name

class District(models.Model):
	district_id = models.CharField(blank=False, max_length=100, primary_key=True)
	district_short = models.CharField(blank=True, max_length=100)
	state = models.ForeignKey(State, related_name='district')
	job_title = models.CharField(blank=True, max_length=100)
	population = models.IntegerField(blank=False, max_length=10, null=True)
	percent_aa = models.DecimalField(blank=True, max_digits=4, decimal_places=2, null=True)
	percent_latino = models.DecimalField(blank=True, max_digits=4, decimal_places=2, null=True)
	percent_obama = models.DecimalField(blank=True, max_digits=4, decimal_places=2, null=True)
	primary_election_date = models.DateField(null=True)
	general_election_date = models.DateField(null=True)
	next_filing_date = models.DateField(blank=True, null=True)
	election_result = models.URLField(blank=True, max_length=500)
	notes = models.TextField(blank=True)
	slug = models.SlugField(blank=True, null=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.district_id)
		super(District, self).save(*args, **kwargs)

	class Meta:
		ordering = ['district_id']

	def __unicode__(self):
		return self.district_id


class Election(models.Model):
	election_name = models.CharField(blank=False, max_length=100, primary_key=True)
	election_year =  models.IntegerField(blank=True, max_length=4, null=True)
	district =  models.ForeignKey(District, related_name='election')
	state = models.ForeignKey(State, related_name='election')
	tier = models.CharField(blank=True, max_length=2)
	election_result = models.URLField(blank=True, max_length=150)
	notes = models.TextField(blank=True)
	slug = models.SlugField(blank=True, null=True)

	def save(self, *args, **kwargs):
			self.slug = slugify(self.election_name)
			super(Election, self).save(*args, **kwargs)


	class Meta:
		ordering = ['election_name']

	def __unicode__(self):
		return self.election_name

class Party(models.Model):
	party_name = models.CharField(blank=False, max_length=100)

	def __unicode__(self):
		return self.party_name

class Candidate(models.Model):
	first_name = models.CharField(blank=True, max_length=100)
	last_name = models.CharField(blank=True, max_length=100)
	image =  models.ImageField(upload_to='candidates', blank=True)
	gender = models.CharField(blank=False, choices=GENDER_CHOICES, max_length=100, default='Not Sure')
	race = models.CharField(blank=False, max_length=100, default='Not Sure')
	party = models.ForeignKey(Party, related_name='candidate')
	is_incumbent = models.CharField(blank=False, choices=BOOL_CHOICES, max_length=100, default='Not Sure')
	is_running = models.CharField(blank=False, choices=BOOL_CHOICES, max_length=100, default='Not Sure')
	is_appointed = models.CharField(blank=False, choices=BOOL_CHOICES, max_length=100, default='Not Sure')
	won_primary = models.CharField(blank=True, choices=BOOL_CHOICES, max_length=100, null=True)
	election = models.ForeignKey(Election, related_name='candidate', null=True)
	first_year_elected = models.IntegerField(blank=True, max_length=4, null=True)
	last_year_elected = models.IntegerField(blank=True, max_length=4, null=True)
	percent_vote = models.IntegerField(blank=True, null=True)
	notes = models.TextField(blank=True)
	slug = models.SlugField(blank=True, null=True)

	def save(self, *args, **kwargs):
		slug_str = "%s %s" % (self.first_name, self.last_name)
		unique_slugify(self, slug_str)
		super(Candidate, self).save(**kwargs)

	class Meta:
		ordering = ['last_name']

	def __unicode__(self):
		return self.last_name + ' ' + self.first_name


class County(models.Model):
	fips_code = models.IntegerField(primary_key=True)
	county_name = models.CharField(blank=False, max_length=100)
	district = models.ForeignKey(District, related_name='counties')
	state = models.ForeignKey(State, related_name='counties')
	notes = models.TextField(blank=True)

	class Meta:
		ordering = ['fips_code']

	def __unicode__(self):
		return self.county_name

