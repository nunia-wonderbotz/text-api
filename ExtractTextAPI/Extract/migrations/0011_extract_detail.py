# Generated by Django 4.1.9 on 2023-06-26 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Extract', '0010_extract_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='extract',
            name='detail',
            field=models.CharField(default='', max_length=70),
        ),
    ]
