from django import forms
from django.contrib import admin
from .models import Members, MembersRole, Events


# Register your models here.
class MembersAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "end_date", "github_link",
                    "image_link", "linkedin_link", "linked_member_role", "start_date")
    search_fields = ['name', 'email']
    readonly_fields = ['id']

    def linked_member_role(self, obj):
        return obj.member_role.title if obj.member_role else None

    linked_member_role.short_description = 'Member Role'

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['member_role'].label_from_instance = lambda obj: obj.title if obj else ''
        return form


class EventsAdmin(admin.ModelAdmin):
    list_display = ("title", "linked_events_cat", "description", "image_link", "start_date", "end_date", "linked_collab",
                    "is_featured")
    search_fields = ['title']
    readonly_fields = ['id']

    def linked_events_cat(self, obj):
        return obj.event_cat.title if obj.event_cat else None

    linked_events_cat.short_description = 'Event Cat'

    def linked_collab(self, obj):
        return obj.collab.name if obj.collab else None
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['event_cat'].label_from_instance = lambda obj: obj.title if obj else ''
        form.base_fields['collab'].label_from_instance = lambda obj: obj.name if obj else ''
        return form


admin.site.register(Members, MembersAdmin)
admin.site.register(Events, EventsAdmin)
