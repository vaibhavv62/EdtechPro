# Generated by Django 3.2.9 on 2021-11-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeadGeneration', '0003_lead_school_college'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='handled_by',
            field=models.CharField(default='Sneha K.', max_length=32),
            preserve_default=False,
        ),
    ]
