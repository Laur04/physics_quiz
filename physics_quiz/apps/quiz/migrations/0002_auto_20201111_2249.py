# Generated by Django 3.0.6 on 2020-11-11 22:49

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='o_l',
            field=models.IntegerField(default=0, verbose_name='Frequency Ol'),
        ),
        migrations.AddField(
            model_name='option',
            name='o_m',
            field=models.IntegerField(default=0, verbose_name='Frequency Om'),
        ),
        migrations.AlterField(
            model_name='option',
            name='name',
            field=models.CharField(choices=[('a', 'Medicine/Health'), ('b', 'Biology'), ('c', 'Chemistry'), ('d', 'Physics'), ('e', 'Astronomy'), ('f', 'Engineering'), ('g', 'English/Writing'), ('h', 'Finance/Business/Consultancy'), ('i', 'Administration/Management'), ('j', 'Arts/Media'), ('k', 'Academia/Education'), ('l', 'Technology/Computer Science'), ('m', 'Law'), ('1', 'Making money'), ('2', 'Helping other people'), ('3', 'Having job security'), ('4', 'Working with people'), ('5', 'Having lots of family time'), ('6', 'Having an exciting job'), ('7', 'Making use of my talents/abilities')], max_length=1, primary_key=True, serialize=False, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='q2_answer',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('a', 'Medicine/Health'), ('b', 'Biology'), ('c', 'Chemistry'), ('d', 'Physics'), ('e', 'Astronomy'), ('f', 'Engineering'), ('g', 'English/Writing'), ('h', 'Finance/Business/Consultancy'), ('i', 'Administration/Management'), ('j', 'Arts/Media'), ('k', 'Academia/Education'), ('l', 'Technology/Computer Science'), ('m', 'Law')], max_length=25),
        ),
    ]