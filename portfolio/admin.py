from django.contrib import admin
from portfolio.models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)