# Generated by Django 4.1.5 on 2023-02-02 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_user_content', '0007_remove_onemaincity_slug_onemaincity_city_id_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onemaincity',
            name='city_id_field',
            field=models.IntegerField(verbose_name='ID'),
        ),
    ]
