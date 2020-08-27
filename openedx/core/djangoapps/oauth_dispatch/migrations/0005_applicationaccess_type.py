# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 18:18


import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth_dispatch', '0004_auto_20180626_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationaccess',
            name='application',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='access', to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
        ),
    ]
