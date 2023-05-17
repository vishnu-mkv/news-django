# Generated by Django 2.1 on 2020-03-14 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headlines', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=25)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
            ],
        ),
    ]