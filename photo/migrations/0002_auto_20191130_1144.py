# Generated by Django 2.2.7 on 2019-11-30 11:44

from django.conf import settings
from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='hashtag',
            field=jsonfield.fields.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name='photo',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
