# Generated by Django 2.2.6 on 2019-11-07 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20191107_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='note',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]
