<<<<<<< HEAD
# Generated by Django 3.1.2 on 2020-10-30 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[('Donor', 'Donor'), ('Receiver', 'Receiver')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='verification_status',
            field=models.BooleanField(default=False),
        ),
    ]
=======
# Generated by Django 3.1.2 on 2020-10-30 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[('Donor', 'Donor'), ('Receiver', 'Receiver')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='verification_status',
            field=models.BooleanField(default=False),
        ),
    ]
>>>>>>> 7804fdbc8beb87c0011895981248dcd449f93126
