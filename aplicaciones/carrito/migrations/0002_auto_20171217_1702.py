# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-17 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito_compra',
            name='precio_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='carrito_compra',
            name='cursos',
            field=models.ManyToManyField(blank=True, to='cursos.Curso'),
        ),
    ]
