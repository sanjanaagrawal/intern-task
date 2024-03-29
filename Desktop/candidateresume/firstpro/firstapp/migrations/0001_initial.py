# Generated by Django 3.0 on 2019-12-08 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='modeltable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=264)),
                ('location', models.CharField(max_length=264)),
                ('education', models.CharField(max_length=264)),
                ('internships', models.CharField(max_length=264)),
                ('trainings', models.CharField(max_length=264)),
                ('projects', models.CharField(max_length=264)),
                ('skills', models.CharField(max_length=264)),
            ],
        ),
    ]
