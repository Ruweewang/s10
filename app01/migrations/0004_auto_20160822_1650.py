# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20160822_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.TextField(default=0, max_length=500),
            preserve_default=False,
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
