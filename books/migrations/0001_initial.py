# Generated by Django 5.1.1 on 2024-09-29 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=100)),
                ('ISBN', models.CharField(max_length=13, unique=True)),
                ('Publisher', models.CharField(max_length=100)),
                ('Page_Count', models.IntegerField()),
                ('Available', models.BooleanField(default=True)),
            ],
        ),
    ]
