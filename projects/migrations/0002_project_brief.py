# Generated by Django 2.0.4 on 2019-01-08 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='brief',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
