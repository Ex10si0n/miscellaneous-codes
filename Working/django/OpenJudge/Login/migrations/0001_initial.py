# Generated by Django 3.1.5 on 2021-01-26 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('passwd', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=100)),
            ],
        ),
    ]
