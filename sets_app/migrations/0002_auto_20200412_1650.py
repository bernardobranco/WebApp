# Generated by Django 3.0.5 on 2020-04-12 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sets_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.TextField(verbose_name='Brand of boat')),
                ('model', models.TextField(verbose_name='Model of boat')),
            ],
        ),
        migrations.AlterField(
            model_name='set',
            name='boat',
            field=models.OneToOneField(help_text='Select boat used for set', null=True, on_delete=django.db.models.deletion.SET_NULL, to='sets_app.Boat'),
        ),
    ]