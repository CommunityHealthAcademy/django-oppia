# Generated by Django 2.2.5 on 2019-11-29 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomField',
            fields=[
                ('id', models.CharField(max_length=100,
                                        primary_key=True,
                                        serialize=False)),
                ('label', models.CharField(max_length=200)),
                ('required', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=0)),
                ('helper_text', models.TextField(blank=True,
                                                 default=None,
                                                 null=True)),
                ('type', models.CharField(choices=[('str', 'String'),
                                                   ('int', 'Integer'),
                                                   ('bool', 'Boolean')],
                                          max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileCustomField',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('value_str', models.TextField(blank=True,
                                               default=None,
                                               null=True)),
                ('value_int', models.IntegerField(blank=True,
                                                  default=None,
                                                  null=True)),
                ('value_bool', models.BooleanField(default=None, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('key_name',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='profile.CustomField')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
