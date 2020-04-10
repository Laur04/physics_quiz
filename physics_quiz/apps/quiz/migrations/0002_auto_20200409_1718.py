# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-09 21:18
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='option',
            fields=[
                ('name', models.CharField(choices=[(b'a', b'Medicine/Health'), (b'b', b'Biology'), (b'c', b'Chemistry'), (b'd', b'Physics'), (b'e', b'Astronomy'), (b'f', b'Engineering'), (b'g', b'English/Writing'), (b'h', b'Finance/Business/Consultancy'), (b'i', b'Administration/Management'), (b'j', b'Arts/Media'), (b'k', b'Academia/Education'), (b'1', b'Making money'), (b'2', b'Helping other people'), (b'3', b'Having job security'), (b'4', b'Working with people'), (b'5', b'Having lots of family time'), (b'6', b'Having an exciting job'), (b'7', b'Making use of my talents/abilities')], max_length=1, primary_key=True, serialize=False, unique=True, verbose_name=b'Name')),
                ('o_1', models.IntegerField(verbose_name=b'Frequency O1')),
                ('o_2', models.IntegerField(verbose_name=b'Frequency O2')),
                ('o_3', models.IntegerField(verbose_name=b'Frequency O3')),
                ('o_4', models.IntegerField(verbose_name=b'Frequency O4')),
                ('o_5', models.IntegerField(verbose_name=b'Frequency O5')),
                ('o_6', models.IntegerField(verbose_name=b'Frequency O6')),
                ('o_7', models.IntegerField(verbose_name=b'Frequency O7')),
                ('o_a', models.IntegerField(verbose_name=b'Frequency Oa')),
                ('o_b', models.IntegerField(verbose_name=b'Frequency Ob')),
                ('o_c', models.IntegerField(verbose_name=b'Frequency Oc')),
                ('o_d', models.IntegerField(verbose_name=b'Frequency Od')),
                ('o_e', models.IntegerField(verbose_name=b'Frequency Oe')),
                ('o_f', models.IntegerField(verbose_name=b'Frequency Of')),
                ('o_g', models.IntegerField(verbose_name=b'Frequency Og')),
                ('o_h', models.IntegerField(verbose_name=b'Frequency Oh')),
                ('o_i', models.IntegerField(verbose_name=b'Frequency Oi')),
                ('o_j', models.IntegerField(verbose_name=b'Frequency Oj')),
                ('o_k', models.IntegerField(verbose_name=b'Frequency Ok')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='q2_answer',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(b'a', b'Medicine/Health'), (b'b', b'Biology'), (b'c', b'Chemistry'), (b'd', b'Physics'), (b'e', b'Astronomy'), (b'f', b'Engineering'), (b'g', b'English/Writing'), (b'h', b'Finance/Business/Consultancy'), (b'i', b'Administration/Management'), (b'j', b'Arts/Media'), (b'k', b'Academia/Education')], max_length=21),
        ),
    ]
