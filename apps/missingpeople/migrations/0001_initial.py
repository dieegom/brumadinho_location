# Generated by Django 2.1.5 on 2019-02-06 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicdate', models.CharField(max_length=999)),
                ('name', models.CharField(max_length=999)),
            ],
        ),
    ]
