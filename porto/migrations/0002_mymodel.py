# Generated by Django 2.2.13 on 2022-02-09 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('RegNumber', models.TextField(primary_key=True, serialize=False)),
                ('Description', models.TextField(null=True)),
            ],
        ),
    ]