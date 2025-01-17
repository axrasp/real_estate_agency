# Generated by Django 2.2.24 on 2022-07-16 12:18
import re

import phonenumbers
from django.db import migrations


def normalize_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().iterator():
        phone = flat.owners_phonenumber
        phone_cleaned = re.sub('[)/(/ /-]', '', phone)
        if phone_cleaned[0] == '8':
            phone_cleaned = '+7' + phone_cleaned[1:]
        phone_parsed = phonenumbers.parse(phone_cleaned, 'RU')
        if phonenumbers.is_valid_number(phone_parsed):
            flat.owner_pure_phone = phone_parsed
        else:
            flat.owner_pure_phone = None
        flat.save()


def clean_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().iterator():
        flat.owner_pure_phone = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20220716_1514'),
    ]

    operations = [
        migrations.RunPython(normalize_phonenumber, clean_phonenumber)
    ]
