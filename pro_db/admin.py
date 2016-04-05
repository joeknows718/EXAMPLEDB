from django.contrib import admin
# Register your models here.
from models import UserProfile, District, County, Candidate, Election, Party, State
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

class UserProfileChangeForm(UserChangeForm):
	class Meta(UserChangeForm.Meta):
		model = UserProfile

class UserProfileAdmin(UserAdmin):
	form = UserProfileChangeForm
	fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('is_approved', 'organization')}),
    )


class DistrictResource(resources.ModelResource):

	class Meta:
		model = District
		skip_unchanged = True
		report_skipped = True
		import_id_fields = ('district_id',)
		exclude = ('slug', )

class DistrictAdmin(ImportExportModelAdmin):
    resource_class = DistrictResource
    prepopulated_fields = {'slug':('district_id',)}
    pass

class CountyResource(resources.ModelResource):

	class Meta:
		model = County
		import_id_fields = ('fips_code',)
		#county = fields.Field(column_name='name')

class CountyAdmin(ImportExportModelAdmin):
    resource_class = CountyResource

    pass

class StateResource(resources.ModelResource):

	class Meta:
		model = State
		import_id_fields = ('state_short',)
		exclude = ('slug', )

class StateAdmin(ImportExportModelAdmin):
    resource_class = StateResource
    prepopulated_fields = {'slug':('state_name',)}

    pass


class CandidateResource(resources.ModelResource):

	class Meta:
		model = Candidate
		skip_unchanged = True
		report_skipped = True
		exclude = ('slug', )


class CandidateAdmin(ImportExportModelAdmin):
	resource_class = CandidateResource
	prepopulated_fields = {'slug':('slug',)}
	pass

class ElectionResource(resources.ModelResource):

	class Meta:
		model = Election
		skip_unchanged = True
		report_skipped = True
		import_id_fields = ('election_name',)
		exclude = ('slug', )

class ElectionAdmin(ImportExportModelAdmin):
	resource_class = ElectionResource
	prepopulated_fields = {'slug':('election_name',)}
	pass

class PartyResource(resources.ModelResource):
	class Meta:
		model = Party

class PartyAdmin(ImportExportModelAdmin):
    resource_class = PartyResource
    pass

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(County, CountyAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Election, ElectionAdmin)
admin.site.register(Party, PartyAdmin)

