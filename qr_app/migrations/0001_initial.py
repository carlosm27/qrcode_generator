# Generated by Django 4.1 on 2022-09-05 20:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QrInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=200)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
