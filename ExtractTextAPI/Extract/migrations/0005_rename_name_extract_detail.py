# Generated by Django 4.1.9 on 2023-06-26 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Extract', '0004_remove_extract_file_extract_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extract',
            old_name='name',
            new_name='detail',
        ),
    ]