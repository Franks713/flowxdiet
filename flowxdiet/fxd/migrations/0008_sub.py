# Generated by Django 5.0.3 on 2024-03-28 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fxd', '0007_rename_query_calorie_foods'),
    ]

    operations = [
        migrations.CreateModel(
            name='sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]