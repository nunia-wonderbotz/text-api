# Generated by Django 4.1.9 on 2023-06-26 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Extract', '0006_remove_extract_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='extract',
            name='file',
            field=models.FileField(blank=True, upload_to='my_file'),
        ),
    ]
