# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_approved', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                (b'objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100, blank=True)),
                ('last_name', models.CharField(max_length=100, blank=True)),
                ('image', models.ImageField(upload_to=b'candidates', blank=True)),
                ('gender', models.CharField(max_length=100, choices=[(b'M', b'M'), (b'F', b'F')])),
                ('ethnicity', models.CharField(max_length=100)),
                ('is_incumbent', models.BooleanField(default=False)),
                ('is_running', models.BooleanField(default=False)),
                ('first_year_elected', models.IntegerField(max_length=4)),
                ('last_year_elected', models.IntegerField(max_length=4)),
                ('percent_vote', models.IntegerField(blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('fips_code', models.IntegerField(serialize=False, primary_key=True)),
                ('county_name', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('district_id', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('district_short', models.CharField(max_length=100, blank=True)),
                ('job_title', models.CharField(max_length=100, blank=True)),
                ('population', models.IntegerField(max_length=10)),
                ('percent_aa', models.IntegerField(blank=True)),
                ('percent_latino', models.IntegerField(blank=True)),
                ('percent_obama', models.IntegerField(blank=True)),
                ('election_year', models.IntegerField(max_length=4)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('election_name', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('election_year', models.IntegerField(max_length=4)),
                ('tier', models.CharField(max_length=2)),
                ('election_result', models.CharField(max_length=150, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('next_election_date', models.DateField()),
                ('district', models.ForeignKey(related_name='district', to='pro_db.District')),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('party_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_short', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('state_name', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(related_name='state', to='pro_db.State'),
        ),
        migrations.AddField(
            model_name='county',
            name='district',
            field=models.ForeignKey(related_name='counties', to='pro_db.District'),
        ),
        migrations.AddField(
            model_name='county',
            name='state',
            field=models.ForeignKey(related_name='counties', to='pro_db.State'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='party',
            field=models.ForeignKey(related_name='party', to='pro_db.Party'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='race',
            field=models.ForeignKey(related_name='election', to='pro_db.Election'),
        ),
    ]
