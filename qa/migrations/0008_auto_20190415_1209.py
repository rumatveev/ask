# Generated by Django 2.1.7 on 2019-04-15 12:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0007_question_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='get_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
