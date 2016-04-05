from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator   

user_approved = user_passes_test(lambda u: u.is_approved, login_url='/not-approved')




class ApprovedMixin(object):
	@method_decorator(user_approved)
	def dispatch(self, *args, **kwargs):
		return super(ApprovedMixin, self).dispatch(*args, **kwargs)
