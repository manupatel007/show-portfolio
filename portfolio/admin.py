from django.contrib import admin
from portfolio.models import Project, NewFields, FollowersField, FollowingField, NotificationsField

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    pass

class NewFieldsAdmin(admin.ModelAdmin):
    pass

class FollowersFieldAdmin(admin.ModelAdmin):
    pass

class FollowingFieldAdmin(admin.ModelAdmin):
    pass

class NotificationsFieldAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(NewFields, NewFieldsAdmin)
admin.site.register(FollowersField, FollowersFieldAdmin)
admin.site.register(FollowingField, ProjectAdmin)
admin.site.register(NotificationsField, NotificationsFieldAdmin)