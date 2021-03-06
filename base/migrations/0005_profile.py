# Generated by Django 3.1.2 on 2020-10-31 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=5)),
                ('positive_date', models.DateField()),
                ('negative_date', models.DateField(blank=True, null=True)),
                ('vaccinated', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True)),
                ('current_health_status', models.CharField(blank=True, choices=[('Normal', 'Normal'), ('Average', 'Average'), ('Critical', 'Critical')], max_length=10, null=True)),
                ('no_of_times_tested', models.IntegerField(default=1)),
                ('reports', models.FileField(upload_to='reports')),
                ('hospital_name', models.CharField(max_length=200)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
