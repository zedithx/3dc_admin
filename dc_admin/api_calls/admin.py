from django import forms
from django.contrib import admin
from .models import Members, MembersRole, Events, Projects


# Register your models here.
class MembersAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "end_date", "github_link",
                    "image_link", "linkedin_link", "linked_member_role", "start_date")
    search_fields = ['name', 'email']
    readonly_fields = ['id']

    def linked_member_role(self, obj):
        return obj.member_role.title if obj.member_role else None

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['member_role'].label_from_instance = lambda obj: obj.title if obj else ''
        return form

    linked_member_role.short_description = 'Member Role'

class EventsAdmin(admin.ModelAdmin):
    list_display = ("title", "linked_events_cat", "description", "image_link", "start_date", "end_date", "linked_collab",
                    "is_featured")
    search_fields = ['title']
    readonly_fields = ['id']

    def linked_events_cat(self, obj):
        return obj.event_cat.title if obj.event_cat else None

    def linked_collab(self, obj):
        return obj.collab.name if obj.collab else None

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['event_cat'].label_from_instance = lambda field: field.title if field else ''
        form.base_fields['collab'].label_from_instance = lambda field: field.name if field else ''
        return form

    linked_events_cat.short_description = 'Event Cat'
    linked_collab.short_description = 'Collab'


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("title", "linked_project_cat", "description", "image_link", "start_date", "end_date", "linked_collab")
    search_fields = ['title']
    readonly_fields = ['id']

    def linked_collab(self, obj):
        return obj.collab.name if obj.collab else None

    def linked_project_cat(self, obj):
        return obj.project_cat.title if obj.project_cat else None

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['project_cat'].label_from_instance = lambda field: field.title if field else ''
        form.base_fields['collab'].label_from_instance = lambda field: field.name if field else ''
        return form

    linked_collab.short_description = 'Collab'
    linked_project_cat.short_description = 'Project Cat'


admin.site.register(Members, MembersAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(Projects, ProjectsAdmin)
