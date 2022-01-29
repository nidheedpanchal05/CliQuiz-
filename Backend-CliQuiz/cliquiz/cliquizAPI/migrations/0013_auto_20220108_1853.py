# Generated by Django 3.1.2 on 2022-01-08 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliquizAPI', '0012_auto_20220107_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='course', to='cliquizAPI.course'),
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='student', to='cliquizAPI.student'),
        ),
    ]