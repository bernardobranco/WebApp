# Generated by Django 3.0.5 on 2020-04-14 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sets_app', '0002_auto_20200412_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='boat',
            field=models.ForeignKey(help_text='Select boat used for set', null=True, on_delete=django.db.models.deletion.SET_NULL, to='sets_app.Boat'),
        ),
    ]
