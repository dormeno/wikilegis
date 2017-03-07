# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 13:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supressamendment',
            name='content',
            field=models.TextField(default='', verbose_name='content'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='segmenttype',
            name='name',
            field=models.CharField(max_length=200, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='segmenttype',
            name='parents',
            field=models.ManyToManyField(related_name='_segmenttype_parents_+', to='core.SegmentType', verbose_name='parent type'),
        ),
        migrations.AlterField(
            model_name='updownvote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuário'),
        ),
    ]