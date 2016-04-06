from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest
from django.views.generic import FormView, CreateView, RedirectView
from django.views.generic import TemplateView, View, DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.list import MultipleObjectMixin, TemplateResponseMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, PasswordChangeForm 
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash 
from decorators import ApprovedMixin
from braces.views import LoginRequiredMixin
from forms import RegisterForm, PasswordRecoveryForm, ContactForm
from forms import DistrictFilterForm, ElectionFilterForm, CandidateFilterForm
from django.contrib.auth import update_session_auth_hash
from models import State, Candidate, Party, Election, District, County
from datetime import date
from django.db.models import Count
from django.db.models import Q
# Create your views here.

#|------------------------Landing / Customer Service  Pages------------------------------------------|
class HomeView(View):
	template_name="index.html"


	def get(self, request, *args, **kwargs): 
		if request.user.is_authenticated():
			return HttpResponseRedirect('/dashboard')
		else:
			context = {}

			return  render(request, self.template_name, context)


class ContactView(FormView):
	template_name = 'contact.html'
	form_class = ContactForm
	success_url = reverse_lazy('thanks')

	def form_valid(self, form):
		form.send_message()
		return super(ContactView, self).form_valid(form)






#|------------------------Report Pages------------------------------------------|
class DashBoardView(LoginRequiredMixin, ApprovedMixin, View):
	template_name = 'dashboard.html'

	def get(self, request, *args, **kwargs): 
		context = {}
		districts_upcoming = District.objects.filter(
			general_election_date__year=date.today().year)

		context['districts_upcoming'] = districts_upcoming.filter(general_election_date__gt=date.today()).order_by(
			'general_election_date')

		context['dist_by_aa'] = districts_upcoming.exclude(percent_aa=None).exclude(percent_aa=0.0)order_by('-percent_aa')[:50]

		context['upcoming_elections'] = Election.objects.filter(district__general_election_date__year=date.today().year).order_by('-district__general_election_date')[:50]

		context['candidate_upcoming'] = Candidate.objects.filter(election__district__general_election_date__gt=date.today()
			).order_by('-election__district__general_election_date')[:50]

		context['candidate_unopposed'] = Candidate.objects.annotate(num_cand=Count('election__candidate')).filter(num_cand__lt=2
			).order_by('-election__district__general_election_date')[:50]

			
		return  render(request, self.template_name, context)


class DistrictReportGen(LoginRequiredMixin,
						ApprovedMixin, 
						FormMixin,
						MultipleObjectMixin,
						TemplateResponseMixin, 
						View):

	queryset = District.objects.all()
	form_class = DistrictFilterForm
	template_name = 'district-reports.html'


	def post(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		if form.is_valid():
			return self.form_valid(form)
		else:
			form_errors = form.errors
			self.object_list = self.get_queryset().order_by('-general_election_date')
			return self.render_to_response(self.get_context_data(form=form, 
																object_list=self.object_list,
																form_errors=form_errors))

	def get(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		self.object_list = self.get_queryset().order_by('-general_election_date')
		return self.render_to_response(self.get_context_data(form=form, object_list=self.object_list))



	def form_valid(self, form):
		queryset = self.get_queryset()
		state_param = form.cleaned_data['state']

		if state_param == 'All States' or state_param == None:
			pass
		else:
			queryset = queryset.filter(state__state_name=state_param)

		aa_param = form.cleaned_data['percentage_aa']

		if aa_param == 0 or aa_param == None:
			pass
		else:
			queryset = queryset.filter(percent_aa__gte=aa_param)

		latino_param = form.cleaned_data['percentage_latino']

		if latino_param == 0 or latino_param == None:
			pass
		else:
			queryset = queryset.filter(percent_latino__gte=latino_param)

		obama_param = form.cleaned_data['obama_share']

		if obama_param == 0 or obama_param == None:
			pass
		else:
			queryset = queryset.filter(percent_obama__gte=obama_param)

		order_param = form.cleaned_data['order_by']

		if order_param == None or order_param == 'Upcoming General Elections':
			queryset = queryset.order_by('-general_election_date')
		elif order_param == 'Upcoming Primary Dates':
			queryset = queryset.order_by('-primary_election_date')
		elif order_param == 'Upcoming Filing Dates':
			queryset = queryset.order_by('-next_filing_date')
		elif order_param == 'Highest percent of African Americans':
			queryset = queryset.order_by('-percent_aa')
		elif order_param == 'Highest percent of Latinos':
			queryset = queryset.order_by('-percent_latino')
		elif order_param == 'Population size (High to Low)':
			queryset = queryset.order_by('-population')
		elif order_param == 'Population size (Low to High)':
			queryset = queryset.order_by('population')
		else:
			queryset = queryset.order_by('-percent_obama')

		self.object_list = queryset

		context = self.get_context_data(object_list=self.object_list, 
										form=form, 
										state_param=state_param,
										aa_param=aa_param,
										latino_param=latino_param,
										obama_param=obama_param,
										order_param=order_param)

		return self.render_to_response(context)

class ElectionReportGen(LoginRequiredMixin,
						ApprovedMixin,
						FormMixin,
						MultipleObjectMixin,
						TemplateResponseMixin,
						View):
	queryset = Election.objects.all()
	form_class = ElectionFilterForm
	template_name = 'election-reports.html'

	def post(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		if form.is_valid():
			return self.form_valid(form)
		else:
			form_errors = form.errors
			self.object_list = self.get_queryset().order_by('-general_election_date')
			return self.render_to_response(self.get_context_data(form=form, 
																object_list=self.object_list,
																form_errors=form_errors))
	def get(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		self.object_list = self.get_queryset().order_by('-district__general_election_date')
		return self.render_to_response(self.get_context_data(form=form, object_list=self.object_list))

	def form_valid(self, form):
		queryset = self.get_queryset()
		state_param = form.cleaned_data['state']

		if state_param == 'All States' or  state_param == None:
			pass
		else:
			queryset = queryset.filter(state__state_name=state_param)

		district_param = form.cleaned_data['district']

		if district_param == 'All Districts' or district_param == None:
			pass
		else:
			queryset = queryset.filter(district__district_id=district_param)


		aa_param = form.cleaned_data['percentage_aa']

		if aa_param == 0 or aa_param == None:
			pass
		else:
			queryset = queryset.filter(district__percent_aa__gte=aa_param)

		latino_param = form.cleaned_data['percentage_latino']

		if latino_param == 0 or latino_param == None:
			pass
		else:
			queryset = queryset.filter(district__percent_latino__gte=latino_param)

		obama_param = form.cleaned_data['obama_share']

		if obama_param == 0 or obama_param == None:
			pass
		else:
			queryset = queryset.filter(district__percent_obama__gte=obama_param)

		challenger_param = form.cleaned_data['challenger_only']

		if challenger_param == True:
			queryset = queryset.annotate(num_cand=Count('candidate')).filter(num_cand__gt=1)
		else:
			pass

		no_challenger_param = form.cleaned_data['no_challenger_only']

		if no_challenger_param == True:
			queryset = queryset.annotate(num_cand=Count('candidate')).filter(num_cand__lt=2)
		else:
			pass

		election_year_param = form.cleaned_data['election_year']
		if election_year_param != None:
			queryset = queryset.filter(election_year=election_year_param)
		else:
			pass

		incumbent_only_param = form.cleaned_data['includes_incumbent']

		if incumbent_only_param == True:
			queryset = queryset.filter(candidate__is_incumbent='Yes').distinct()
		else:
			pass

		no_incument_param = form.cleaned_data['does_not_include_incumbent']

		if no_incument_param == True:
			queryset = queryset.filter(~Q(candidate__is_incumbent='Yes')).distinct()


		year_param = form.cleaned_data['election_year']

		if year_param != None:
			pass
		else:
			queryset = queryset.filter(election__election_year=year_param)

		order_param = form.cleaned_data['order_by']

		if order_param == None or order_param == 'Upcoming General Elections':
			queryset = queryset.order_by('-district__general_election_date')
		elif order_param == 'Upcoming Primary Dates':
			queryset = queryset.order_by('-district__primary_election_date')
		elif order_param == 'Upcoming Filing Dates':
			queryset = queryset.order_by('-district__next_filing_date')
		elif order_param == 'Highest percent of African Americans':
			queryset = queryset.order_by('-district__percent_aa')
		elif order_param == 'Highest percent of Latinos':
			queryset = queryset.order_by('-district__percent_latino')
		elif order_param == 'Population size (High to Low)':
			queryset = queryset.order_by('-district__population')
		elif order_param == 'Population size (Low to High)':
			queryset = queryset.order_by('district__population')
		else:
			queryset = queryset.order_by('-district__percent_obama')

		self.object_list = queryset

		context = self.get_context_data(object_list=self.object_list, 
										form=form, 
										state_param=state_param,
										district_param=district_param,
										aa_param=aa_param,
										latino_param=latino_param,
										obama_param=obama_param,
										order_param=order_param,
										challenger_param=challenger_param,
										no_challenger_param=no_challenger_param,
										incumbent_only_param=incumbent_only_param,
										no_incument_param=no_incument_param,
										election_year_param=election_year_param)

		return self.render_to_response(context)

class CandidateReportGen(LoginRequiredMixin,
						ApprovedMixin,
						FormMixin,
						MultipleObjectMixin,
						TemplateResponseMixin,
						View):

	queryset = Candidate.objects.all()
	form_class = CandidateFilterForm
	template_name = 'candidate-reports.html'

	def post(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		if form.is_valid():
			return self.form_valid(form)
		else:
			form_errors = form.errors
			self.object_list = self.get_queryset().order_by('-election__district__general_election_date')
			return self.render_to_response(self.get_context_data(form=form, 
																object_list=self.object_list,
																form_errors=form_errors))

	def get(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		self.object_list = self.get_queryset().order_by('-election__district__general_election_date')
		return self.render_to_response(self.get_context_data(form=form, object_list=self.object_list))

	def form_valid(self, form):
		queryset = self.get_queryset()
		state_param = form.cleaned_data['state']

		if state_param == 'All States' or  state_param == None:
			pass
		else:
			queryset = queryset.filter(election__state__state_name=state_param)

		district_param = form.cleaned_data['district']

		if district_param == 'All Districts' or district_param == None:
			pass
		else:
			queryset = queryset.filter(election__district__district_id=district_param)

		aa_param = form.cleaned_data['percentage_aa']

		if aa_param == 0 or aa_param == None:
			pass
		else:
			queryset = queryset.filter(election__district__percent_aa__gte=aa_param)

		latino_param = form.cleaned_data['percentage_latino']

		if latino_param == 0 or latino_param == None:
			pass
		else:
			queryset = queryset.filter(election__district__percent_latino__gte=latino_param)

		obama_param = form.cleaned_data['obama_share']

		if obama_param == 0 or obama_param == None:
			pass
		else:
			queryset = queryset.filter(election__district__percent_obama__gte=obama_param)

		is_incument_param = form.cleaned_data['is_incumbent']

		if is_incumbent_param == True:
			queryset = queryset.filter(is_incument='Yes')
		else:
			pass
		won_primary_param = form.cleaned_data['won_primary']

		if won_primary_param == True:
			queryset = queryset.filter(won_primary='Yes')
		else:
			pass

		no_incument_param = form.cleaned_data['not_incumbent']

		if no_incument_param == True:
			queryset = queryset.filter(Q(is_incument='No') | Q(is_incument='Not Sure'))
		else:
			pass

		opposed_param = form.cleaned_data['opposed_only']

		if opposed_param == True:
			queryset = queryset.annotate(num_cand=Count('election_candidate')).filter(num_cand__gt=1)
		else:
			pass

		unopposed_param = form.cleaned_data['unopposed_only']

		if unopposed_param == True:
			queryset = queryset.annotate(num_cand=Count('election_candidate')).filter(num_cand__gt=1)
		else:
			pass

		year_param = form.cleaned_data['election_year']

		if year_param != None:
			pass
		else:
			queryset = queryset.filter(election__election_year=year_param)


		order_param = form.cleaned_data['order_by']

		if order_param == None or order_param == 'Upcoming General Elections':
			queryset = queryset.order_by('-election__district__general_election_date')
		elif order_param == 'Upcoming Primary Dates':
			queryset = queryset.order_by('-election__district__primary_election_date')
		elif order_param == 'Upcoming Filing Dates':
			queryset = queryset.order_by('-election__district__next_filing_date')
		elif order_param == 'Highest percent of African Americans':
			queryset = queryset.order_by('-election__district__percent_aa')
		elif order_param == 'Highest percent of Latinos':
			queryset = queryset.order_by('-election__district__percent_latino')
		elif order_param == 'Population size (High to Low)':
			queryset = queryset.order_by('-election__district__population')
		elif order_param == 'Population size (Low to High)':
			queryset = queryset.order_by('election__district__population')
		else:
			queryset = queryset.order_by('-election__district__percent_obama')


		self.object_list = queryset

		context = self.get_context_data(object_list=self.object_list, 
										form=form,
										district_param=district_param,
										state_param=state_param,
										aa_param=aa_param,
										latino_param=latino_param,
										obama_param=obama_param,
										order_param=order_param,
										is_incumbent_param=is_incumbent_param,
										no_incument_param=no_incument_param,
										opposed_param=opposed_param,
										unopposed_param=unopposed_param)

		return self.render_to_response(context)






#|------------------------Individual Profile Pages------------------------------------------|

class StateDetailView(LoginRequiredMixin, ApprovedMixin, DetailView):
	template_name = 'state_details.html'
	model = State
	context_object_name = 'state'


class DistrictDetailView(LoginRequiredMixin, ApprovedMixin, DetailView):
	template_name = 'district_details.html'
	model = District
	context_object_name = 'district'


class ElectionDetailView(LoginRequiredMixin, ApprovedMixin, DetailView):
	template_name = 'election_detail.html'
	model = Election
	context_object_name = 'election'


class CandidateDetailView(LoginRequiredMixin, ApprovedMixin, DetailView):
	template_name = 'candidate_detail.html'
	model = Candidate
	context_object_name = 'candidate'




#|-----------------------ACCESS CONTROL-----------------------------------------|
class RegistrationView(FormView):
	template_name = 'registration.html'
	form_class = RegisterForm
	success_url = reverse_lazy('post-reg')

	def form_valid(self, form):
		saved_user = form.save()
		print saved_user.password
		user = authenticate(
			username = saved_user.username,
			password = form.cleaned_data['password1'])
		login(self.request, user)
		form.notify_admin()
		form.notify_user() 
		return HttpResponseRedirect(self.get_success_url())


class LoginView(FormView):
	template_name = 'login.html'
	form_class = AuthenticationForm
	success_url = reverse_lazy('dashboard')

	def form_valid(self, form):
		user = form.get_user()
		login(self.request, user)
		return super(LoginView, self).form_valid(form)

class LogoutView(RedirectView):
	permanent = False 
	url =  reverse_lazy('index')

	def get(self, request, *args, **kwargs):
		logout(request)
		return super(LogoutView, self).get(request, args, kwargs)

class PasswordRecoveryView(FormView):
	template_name = 'password_recovery.html'
	form_class = PasswordRecoveryForm
	success_url = reverse_lazy('login')
	def form_valid(self, form):
		form.reset_email()
		return super(PasswordRecoveryView, self).form_valid(form)

class SettingsView(LoginRequiredMixin, ApprovedMixin, FormView):
	template_name = 'settings.html'
	form_class = PasswordChangeForm
	success_url = reverse_lazy('dashboard')
	login_url = '/login/'


	def get_form(self, form_class):
		return form_class(user=self.request.user, **self.get_form_kwargs())

	def form_valid(self, form):
		form.save()
		update_session_auth_hash(self.request, form.user)
		return super(SettingsView, self).form_valid(form)

class ThanksView(View):
	template_name="thanks.html"

	def get(self, request, *args, **kwargs): 
		context = {}
		return  render(request, self.template_name, context)

class NotApprovedView(TemplateView):
	template_name = 'not-approved.html'

class PostRegisterView(TemplateView):
	template_name = 'post-reg.html'
