from django.conf.urls import patterns, url
from pro_db import views

urlpatterns = patterns('',
	url(r'^$', views.HomeView.as_view(), name='index'),
	url(r'^register/', views.RegistrationView.as_view(), name='register'),
	url(r'^login/', views.LoginView.as_view(), name='login'),
	url(r'^logout/', views.LogoutView.as_view(), name='logout'),
	url(r'^settings/', views.SettingsView.as_view(), name='settings'),
	url(r'^recover-password/', views.PasswordRecoveryView.as_view(), name='recover-password'),
	url(r'^elections/(?P<slug>[-\w]+)/$', views.ElectionDetailView.as_view(), name='election_detail'),
	url(r'^districts/(?P<slug>[-\w]+)/$', views.DistrictDetailView.as_view(), name='district_detail'),
	url(r'^state/(?P<slug>[-\w]+)/$', views.StateDetailView.as_view(), name='state_detail'),
	url(r'^candidates/(?P<slug>[-\w]+)/$', views.CandidateDetailView.as_view(), name='candidate_detail'),
	url(r'^contact/', views.ContactView.as_view(), name='contact'),
	url(r'^not-approved/', views.NotApprovedView.as_view(), name='not-approved'),
	url(r'^thanks-for-registering/', views.PostRegisterView.as_view(), name='post-reg'),
	url(r'^dashboard/', views.DashBoardView.as_view(), name='dashboard'),
	url(r'district-reports/', views.DistrictReportGen.as_view(), name='district_reports'),
	url(r'election-reports/', views.ElectionReportGen.as_view(), name='election_reports'),
	url(r'candidate-reports/', views.CandidateReportGen.as_view(), name='candidate_reports'),
	url(r'thanks/', views.ThanksView.as_view(), name='thanks'),
	)
