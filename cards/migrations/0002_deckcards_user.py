# Generated by Django 3.1.7 on 2021-03-10 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deckcards',
            name='user',
            field=models.CharField(default='nobody', max_length=100),
        ),
    ]