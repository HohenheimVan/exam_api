# Generated by Django 2.1.5 on 2019-01-12 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esheets', '0003_auto_20190112_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentresponse',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='esheets.TestQuestion'),
        ),
    ]
