# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20160823_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='head_img',
            field=models.ImageField(upload_to=b'/statics/imgs/upload/'),
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
