# Generated by Django 4.2.7 on 2024-11-11 07:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_settings_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created_AT', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'NewsLetter',
                'verbose_name_plural': 'NewsLetters',
            },
        ),
    ]