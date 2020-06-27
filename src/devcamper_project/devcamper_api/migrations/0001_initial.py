# Generated by Django 3.0.4 on 2020-03-19 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bootcamps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('address', models.TextField()),
                ('zipcode', models.CharField(blank=True, max_length=6)),
                ('website', models.URLField()),
                ('phone', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('description', models.CharField(max_length=500)),
                ('careers', models.CharField(max_length=50)),
                ('housing', models.BooleanField()),
                ('jobAssistance', models.BooleanField()),
                ('jobGuarantee', models.BooleanField()),
                ('acceptGi', models.BooleanField()),
            ],
        ),
    ]