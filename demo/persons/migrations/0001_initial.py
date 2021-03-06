# Generated by Django 3.1 on 2020-08-22 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
