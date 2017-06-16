# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nazwa Kategorii')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name=b'Odno\xc5\x9bnik')),
                ('icon', models.ImageField(upload_to=b'icons', verbose_name=b'Ikonka Kategorii', blank=True)),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategorie',
            },
            bases=None,
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'Tytu\xc5\x82')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name=b'Odno\xc5\x9bnik')),
                ('text', models.TextField(verbose_name=b'Tre\xc5\x9b\xc4\x87')),
                ('posted_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Data dodania')),
                ('categories', models.ManyToManyField(to='news.Category', verbose_name=b'Kategorie')),
            ],
            options={
                'verbose_name': 'Wiadomo\u015b\u0107',
                'verbose_name_plural': 'Wiadomo\u015bci',
            },
            bases=None,
        ),
    ]
