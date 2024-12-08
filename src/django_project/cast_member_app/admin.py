from django.contrib import admin
from django_project.cast_member_app.models import CastMember

class CastMemberAdmin(admin.ModelAdmin):
    pass

admin.site.register(CastMember, CastMemberAdmin)