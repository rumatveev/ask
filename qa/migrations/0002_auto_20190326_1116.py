# Generated by Django 2.1.7 on 2019-03-26 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='qa.Answer'),
        ),
    ]
