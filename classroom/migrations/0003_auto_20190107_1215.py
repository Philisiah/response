# Generated by Django 2.0.4 on 2019-01-07 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_auto_20190107_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentanswer',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='classroom.Answer'),
        ),
    ]