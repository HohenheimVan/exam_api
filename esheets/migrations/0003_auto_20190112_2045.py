# Generated by Django 2.1.5 on 2019-01-12 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esheets', '0002_studentresponse_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenttestgrade',
            name='student_test',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='esheets.StudentTest'),
        ),
    ]
