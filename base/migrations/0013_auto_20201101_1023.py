# Generated by Django 3.1.2 on 2020-11-01 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_user_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='place',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]