# Generated by Django 3.2.2 on 2021-05-07 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
