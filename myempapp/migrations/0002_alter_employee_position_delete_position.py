# Generated by Django 4.0.4 on 2022-05-08 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myempapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('software engineer', 'SOFTWARE ENGINEER'), ('web developer', 'WEB DEVELOPER'), ('technical engineer', 'TECHNICAL ENGINEER'), ('data scientist', 'DATA SCIENTIST')], default='software engineer', max_length=100),
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]
