# Generated by Django 4.2 on 2023-04-23 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Names', models.EmailField(max_length=254, unique=True)),
                ('Username', models.CharField(max_length=50, unique=True)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
