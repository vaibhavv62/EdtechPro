# Generated by Django 3.2.9 on 2021-11-17 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeadGeneration', '0004_lead_handled_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='course_interested',
            field=models.CharField(choices=[('Python', 'Python'), ('Java', 'Java'), ('C', 'C'), ('C++', 'C++'), ('Data Structures', 'Data Structures'), ('UI(FrontEnd)', 'UI(FrontEnd)'), ('Aptitude', 'Aptitude'), ('AWS(Cloud Computing)', 'AWS(Cloud Computing)'), ('Spoken English', 'Spoken English')], max_length=32),
        ),
        migrations.AlterField(
            model_name='lead',
            name='current_status_notes',
            field=models.CharField(max_length=128),
        ),
    ]
