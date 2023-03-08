# Generated by Django 4.1.5 on 2023-02-01 08:15

from django.db import migrations, models
import main_user_content.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_user_content', '0002_alter_mainusercontent_main_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelephoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone_number', models.IntegerField(validators=[main_user_content.models.telephone_validator], verbose_name='Номер телефона начиная с 8')),
            ],
            options={
                'verbose_name': 'Номер телефона',
                'verbose_name_plural': 'Номера телефонов',
            },
        ),
        migrations.AlterField(
            model_name='mainusercontent',
            name='slug',
            field=models.SlugField(max_length=80, verbose_name='url slug'),
        ),
    ]
