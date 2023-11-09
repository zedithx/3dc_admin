# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EventMember(models.Model):
    id = models.TextField(primary_key=True)
    member = models.ForeignKey('Members', models.DO_NOTHING)
    event = models.ForeignKey('Events', models.DO_NOTHING)
    role = models.TextField()

    class Meta:
        managed = False
        db_table = 'Event_Member'


class Events(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField()
    event_cat = models.ForeignKey('EventsCat', models.DO_NOTHING, db_column='event_cat', to_field='title')
    description = models.TextField()
    image_link = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    collab = models.ForeignKey('Organisations', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Events'


class EventsCat(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(unique=True)
    description = models.TextField()
    image_link = models.TextField()
    color = models.TextField()

    class Meta:
        managed = False
        db_table = 'Events_Cat'


class Members(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()
    email = models.TextField()
    end_date = models.DateTimeField(blank=True, null=True)
    github_link = models.TextField(blank=True, null=True)
    image_link = models.TextField()
    linkedin_link = models.TextField(blank=True, null=True)
    member_role = models.ForeignKey('MembersRole', models.DO_NOTHING, db_column='member_role', to_field='title')
    start_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Members'


class MembersRole(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(unique=True)
    image_link = models.TextField()
    color = models.TextField()

    class Meta:
        managed = False
        db_table = 'Members_Role'


class Organisations(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()
    poc_name = models.TextField(db_column='POC_name', blank=True, null=True)  # Field name made lowercase.
    poc_contact = models.IntegerField(db_column='POC_contact', blank=True, null=True)  # Field name made lowercase.
    poc_email = models.TextField(db_column='POC_email', unique=True, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Organisations'


class Posts(models.Model):
    id = models.TextField(primary_key=True)
    author = models.ForeignKey(Members, models.DO_NOTHING)
    image_link = models.TextField()
    title = models.TextField()
    date_created = models.DateTimeField()
    caption = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Posts'


class ProjectMember(models.Model):
    id = models.TextField(primary_key=True)
    member = models.ForeignKey(Members, models.DO_NOTHING)
    proj = models.ForeignKey('Projects', models.DO_NOTHING)
    role = models.TextField()

    class Meta:
        managed = False
        db_table = 'Project_Member'


class Projects(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField()
    project_cat = models.ForeignKey('ProjectsCat', models.DO_NOTHING, db_column='project_cat', to_field='title')
    description = models.TextField()
    image_link = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    collab = models.ForeignKey(Organisations, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Projects'


class ProjectsCat(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(unique=True)
    description = models.TextField()
    image_link = models.TextField()
    color = models.TextField()

    class Meta:
        managed = False
        db_table = 'Projects_Cat'


class PrismaMigrations(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    checksum = models.CharField(max_length=64)
    finished_at = models.DateTimeField(blank=True, null=True)
    migration_name = models.CharField(max_length=255)
    logs = models.TextField(blank=True, null=True)
    rolled_back_at = models.DateTimeField(blank=True, null=True)
    started_at = models.DateTimeField()
    applied_steps_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_prisma_migrations'
