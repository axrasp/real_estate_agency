# Generated by Django 2.2.24 on 2022-07-28 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20220728_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='text',
            field=models.TextField(blank=True, verbose_name='Текст жалобы'),
        ),
    ]
