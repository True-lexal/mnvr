# Generated by Django 4.1.5 on 2023-02-15 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customusergroup_alter_customusers_patronymic_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customusers',
            name='groups',
        ),
        migrations.AddField(
            model_name='customusers',
            name='groups',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.customusergroup', verbose_name='Группа'),
        ),
    ]
