# Generated by Django 3.1.14 on 2023-11-02 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('allsvusdwebsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuickLinkCardInfo',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='allsvusdwebsite_quicklinkcardinfo', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(default='Title', max_length=50)),
                ('body_text', models.CharField(default='text body', max_length=500)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.DeleteModel(
            name='Hello',
        ),
    ]
