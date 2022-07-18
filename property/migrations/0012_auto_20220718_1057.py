# Generated by Django 2.2.24 on 2022-07-18 07:57

from django.db import migrations


def clone_owner_data(apps, scheme_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(name=flat.owner,
                                    owner_pure_phone=flat.owner_pure_phone,
                                    owners_phonenumber=flat.owners_phonenumber)


def delete_owners_data(apps, scheme_editor):
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all():
        owner.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20220718_1044'),
    ]

    operations = [
        migrations.RunPython(clone_owner_data, )
    ]
