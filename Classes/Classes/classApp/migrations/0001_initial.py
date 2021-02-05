# Generated by Django 3.1.6 on 2021-02-05 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('course_number', models.IntegerField()),
                ('instructor_name', models.CharField(max_length=50)),
                ('duration', models.FloatField(max_length=4)),
            ],
        ),
    ]
