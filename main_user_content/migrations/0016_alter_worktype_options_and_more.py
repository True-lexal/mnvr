# Generated by Django 4.1.5 on 2023-02-07 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_user_content', '0015_worktype_alter_mainusercontent_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='worktype',
            options={'verbose_name': 'Тип работ', 'verbose_name_plural': 'Тип работы'},
        ),
        migrations.AlterField(
            model_name='maincontentreview',
            name='work_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main_user_content.worktype', verbose_name='Вид работ'),
        ),
        migrations.AlterField(
            model_name='mainusercontent',
            name='preview_img',
            field=models.ImageField(blank=True, null=True, upload_to='type-preview/%Y/%m/%d/', verbose_name='Картинка превью в списке услуг'),
        ),
    ]
