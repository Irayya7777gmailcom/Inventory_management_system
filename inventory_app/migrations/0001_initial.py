# Generated by Django 5.1.2 on 2024-10-16 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
