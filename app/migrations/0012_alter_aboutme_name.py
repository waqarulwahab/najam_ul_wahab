# Generated by Django 5.1.1 on 2024-10-16 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_achievementssection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='name',
            field=models.CharField(blank=True, default='NAJAM UL WAHAB', max_length=255, null=True),
        ),
    ]
