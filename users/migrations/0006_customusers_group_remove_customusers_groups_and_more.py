# Generated by Django 4.1.5 on 2023-02-17 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0005_alter_customusers_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusers',
            name='group',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.customusergroup', verbose_name='Группа'),
        ),
        migrations.RemoveField(
            model_name='customusers',
            name='groups',
        ),
        migrations.AddField(
            model_name='customusers',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
    ]