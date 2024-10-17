# Generated by Django 5.1.1 on 2024-10-11 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_project_detail_description_project_detail_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='client_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
