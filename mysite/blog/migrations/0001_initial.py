# Generated by Django 3.2.13 on 2022-05-10 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('Content', models.TextField()),
                ('author', models.CharField(max_length=13)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
