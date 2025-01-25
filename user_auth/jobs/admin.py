from django.contrib import admin
from .models import Resume, JobApplication

# Register your models here.

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'file', 'id')
    search_fields = ('user__username',)
    list_filter = ('user',)

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job_seeker', 'employer', 'resume', 'applied_on', 'id')
    search_fields = ('job_seeker__username', 'employer__username')
    list_filter = ('job_seeker', 'employer', 'applied_on')

# Register the models with the admin site
admin.site.register(Resume, ResumeAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
