# Generated by Django 4.2.9 on 2024-05-05 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='view2',
            field=models.ImageField(blank=True, null=True, upload_to='item_view2'),
        ),
    ]
