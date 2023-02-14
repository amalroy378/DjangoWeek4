# Generated by Django 4.1.5 on 2023-01-15 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_name', models.CharField(max_length=200)),
                ('actor_industry', models.CharField(max_length=200)),
                ('actor_img', models.ImageField(upload_to='actors')),
            ],
        ),
    ]