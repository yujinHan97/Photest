# Generated by Django 2.2.4 on 2019-11-29 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='likeCnt',
            new_name='rewardCnt',
        ),
    ]
