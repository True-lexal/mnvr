# Generated by Django 4.1.5 on 2023-02-07 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_user_content', '0017_alter_maincontentreview_work_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worktype',
            old_name='work_type',
            new_name='work_type_name',
        ),
    ]
