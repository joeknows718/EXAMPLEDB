from django import forms 
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm 
from models import UserProfile as User
from models import District, Candidate, Election, State 

from django.utils.crypto import get_random_string

ISSUE_CHOICES = (('District', 'District'),
				('Elections', 'Elections'),
				('Candidates', 'Candidates'))

class ContactForm(forms.Form):
	name = forms.CharField(required=True)
	email = forms.CharField(widget=forms.EmailInput(), required=True)
	organization = forms.CharField(required=False)
	issue = forms.CharField(widget=forms.Textarea(), required=True)
	page = forms.CharField(required=False)
	area = forms.ChoiceField(choices=ISSUE_CHOICES, required=True)
	comments = forms.CharField(widget=forms.Textarea(), required=False)

	def send_message(self):
		name = self.cleaned_data['name']
		email = self.cleaned_data['email']
		organization = self.cleaned_data['organization']
		issue = self.cleaned_data['issue']
		comments = self.cleaned_data['comments']
		page = self.cleaned_data['page']
		area = self.cleaned_data['area']
		message = '''
			New Message from {name} @ {email}
			Organization: {organization}
			Issue Area: {area}
			Page: {page}
			Issue Description: {issue}
			Comments: {comments}
		'''.format(name=name,
			email=email,
			organization=organization,
			area=area,
			page=page,
			issue=issue,
			comments=comments)
		send_mail('NEW CONTACT FORM SUBMISSION',
			message,
			'prosecutordb@colorofchange.org',
			['prosecutordb@colorofchange.org', 'joe.carrano@colorofchange.org'])



class RegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)

	#error_messages = {
     #   'password_mismatch': ("The two password fields didn't match."),
      #  }

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'organization', 'password1', 'password2')

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.organization = self.cleaned_data['organization']
		user.set_password(self.cleaned_data["password1"])


		if commit:
			user.save()

		return user

	def notify_admin(self):
		username = self.cleaned_data['username']
		first_name = self.cleaned_data['first_name']
		last_name = self.cleaned_data['last_name']
		email = self.cleaned_data['email']
		organization = self.cleaned_data['organization']
		body = """New user registered as {username}:
		First Name: {first_name}
		Last Name: {last_name}
		Email: {email}
		Organization: {organization}""".format(username=username,
			first_name=first_name,
			last_name=last_name,
			email=email,
			organization=organization)
		send_mail('New user registration NEED REVIEW',
			body,
			'prosecutordb@colorofchange.org',
			['prosecutordb@colorofchange.org', 'joe.carrano@colorofchange.org'])

	def notify_user(self):
		first_name = self.cleaned_data['first_name']
		email = self.cleaned_data['email']

		body = """Hey {first_name},

		Thanks for registering for the Prosecutor Accountability Database powered by ColorOfChange! Your request for access has been received.

		Please allow for up to 2 business days for your access to be granted. If you have any questions, please reach out to us at prosecutordb@colorofchange.org

		Best,

		The ColorOfChange team. """.format(first_name=first_name)
		send_mail('Thanks for registering with the Prosecutor Database',
			body,
			'prosecutordb@colorofchange.org',
			[email])



		


class PasswordRecoveryForm(forms.Form):
	email = forms.EmailField(required=False)

	def clean_email(self):
		try:
			return User.objects.get(email=self.cleaned_data['email'])
		except User.DoesNotExist:
			raise forms.ValidationError("Can't find user based on the email")
		return self.cleaned_data['email']


	def reset_email(self):
		user = self.cleaned_data['email']

		password =  get_random_string(length=8)
		user.set_password(password)
		user.save()

		body = """
 Sorry you are having issues with your account. Below is your username and
 new password:
 Username: {username}
 Password: {password}
 You can login here: http://url.com/login/
 Change your password here: http://url.com/settings/
 """.format(username=user.username, password=password)
		send_mail(
			'[NameOfApp] Password Reset', body, 'prosecutordb@colorofchange.org',
			[user.email])





ORDER_CHOICES = (('Upcoming General Elections','Upcoming General Elections'),
						('Upcoming Primary Dates','Upcoming Primary Dates'),
						('Upcoming Filing Dates','Upcoming Filing Dates'),
						('Population size (High to Low)','Population size (High to Low)'),
						('Population size (Low to High)','Population size (Low to High)'),
						('Highest percent of African Americans','Highest percent of African Americans'),
						('Highest percent of Latinos','Highest percent of Latinos'),
						('Obama Vote Share','Obama Vote Share'),
						)

class DistrictFilterForm(forms.Form):


	state = forms.ModelChoiceField(queryset=State.objects.order_by('state_name'),
		to_field_name="state_name",
		empty_label="All States",
		required=False)

	order_by =  forms.ChoiceField(choices=ORDER_CHOICES, required=False)
	percentage_aa = forms.IntegerField(min_value=0, max_value=100, required=False)
	percentage_latino = forms.IntegerField(min_value=0, max_value=100, required=False)
	pop_gt = forms.IntegerField(min_value=0, required=False)
	pop_lt = forms.IntegerField(min_value=0, required=False)
	obama_share = forms.IntegerField(min_value=0, max_value=100, required=False)


class ElectionFilterForm(forms.Form):
	state = forms.ModelChoiceField(queryset=State.objects.order_by('state_name'),
		to_field_name="state_name",
		empty_label="All States",
		required=False)

	district = forms.ModelChoiceField(queryset=District.objects.all(),
		empty_label="All Districts",
		required=False)

	order_by =  forms.ChoiceField(choices=ORDER_CHOICES, required=False)
	percentage_aa = forms.IntegerField(min_value=0, max_value=100, required=False)
	percentage_latino = forms.IntegerField(min_value=0, max_value=100, required=False)
	pop_gt = forms.IntegerField(min_value=0, required=False)
	pop_lt = forms.IntegerField(min_value=0, required=False)
	obama_share = forms.IntegerField(min_value=0, max_value=100, required=False)
	challenger_only = forms.BooleanField(required=False)
	no_challenger_only = forms.BooleanField(required=False)
	includes_incumbent = forms.BooleanField(required=False)
	does_not_include_incumbent = forms.BooleanField(required=False)
	election_year = forms.ChoiceField(choices=[(x, x) for x in range(2016, 2022)])


class CandidateFilterForm(forms.Form):
	state = forms.ModelChoiceField(queryset=State.objects.order_by('state_name'),
		to_field_name="state_name",
		empty_label="All States",
		required=False)

	district = forms.ModelChoiceField(queryset=District.objects.all(),
		empty_label="All Districts",
		required=False)

	election_year = forms.ChoiceField(choices=[(x, x) for x in range(1, 32)])

	order_by =  forms.ChoiceField(choices=ORDER_CHOICES, required=False)
	percentage_aa = forms.IntegerField(min_value=0, max_value=100, required=False)
	percentage_latino = forms.IntegerField(min_value=0, max_value=100, required=False)
	pop_gt = forms.IntegerField(min_value=0, required=False)
	pop_lt = forms.IntegerField(min_value=0, required=False)
	obama_share = forms.IntegerField(min_value=0, max_value=100, required=False)
	is_incumbent = forms.BooleanField(required=False)
	not_incumbent = forms.BooleanField(required=False)
	won_primary = forms.BooleanField(required=False)
	opposed_only = forms.BooleanField(required=False)
	unopposed_only = forms.BooleanField(required=False)




