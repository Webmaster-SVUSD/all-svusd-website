# Generated by Django 3.1.14 on 2023-11-22 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allsvusdwebsite', '0025_auto_20231122_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventcardinfo',
            old_name='donate_link',
            new_name='link_1',
        ),
        migrations.RenameField(
            model_name='eventcardinfo',
            old_name='register_here',
            new_name='link_2',
        ),
        migrations.RenameField(
            model_name='eventcardinfo',
            old_name='supplies_to_org_link',
            new_name='link_3',
        ),
        migrations.RenameField(
            model_name='eventcardinfo',
            old_name='volunteer_link',
            new_name='link_4',
        ),
        migrations.AddField(
            model_name='eventcardinfo',
            name='link2_info',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='eventcardinfo',
            name='link3_info',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='eventcardinfo',
            name='link4_info',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]
