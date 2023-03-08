# Generated by Django 4.1.5 on 2023-02-02 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_user_content', '0006_onemaincity_slug_alter_onemaincity_main_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onemaincity',
            name='slug',
        ),
        migrations.AddField(
            model_name='onemaincity',
            name='city_id_field',
            field=models.SlugField(default=1, max_length=80, verbose_name='ID'),
            preserve_default=False,
        ),
    ]