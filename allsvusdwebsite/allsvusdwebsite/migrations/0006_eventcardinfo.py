# Generated by Django 3.1.14 on 2023-12-01 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('allsvusdwebsite', '0005_auto_20231103_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCardInfo',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='allsvusdwebsite_eventcardinfo', serialize=False, to='cms.cmsplugin')),
                ('image', models.ImageField(blank=True, null=True, upload_to='quick_link_images')),
                ('title', models.CharField(default='Title', max_length=500)),
                ('date', models.CharField(default='', max_length=500)),
                ('time', models.CharField(default='', max_length=500)),
                ('link1_button_info', models.CharField(blank=True, default='', max_length=500)),
                ('link_1', models.TextField(blank=True, default='', max_length=5000)),
                ('link2_button_info', models.CharField(blank=True, default='', max_length=500)),
                ('link_2', models.TextField(blank=True, default='', max_length=5000)),
                ('link3_button_info', models.CharField(blank=True, default='', max_length=500)),
                ('link_3', models.TextField(blank=True, default='', max_length=5000)),
                ('link4_button_info', models.CharField(blank=True, default='', max_length=500)),
                ('link_4', models.TextField(blank=True, default='', max_length=5000)),
                ('text_body', models.TextField(default='Text Body', max_length=5000)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
