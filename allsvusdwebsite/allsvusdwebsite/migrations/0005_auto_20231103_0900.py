# Generated by Django 3.1.14 on 2023-11-03 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allsvusdwebsite', '0004_quicklinkcardinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quicklinkcardinfo',
            name='image',
            field=models.ImageField(null=True, upload_to='quick_link_images'),
        ),
    ]