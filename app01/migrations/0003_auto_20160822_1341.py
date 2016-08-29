# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20160822_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='head_img',
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(to='app01.Article'),
        ),
        migrations.AlterField(
            model_name='thumbup',
            name='article',
            field=models.ForeignKey(to='app01.Article'),
        ),
    ]
