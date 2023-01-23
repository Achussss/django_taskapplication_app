# Generated by Django 4.1.3 on 2023-01-04 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.CharField(max_length=200)),
            ],
        ),
    ]