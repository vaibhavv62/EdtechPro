# Generated by Django 3.2.9 on 2021-11-16 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type_of_lead', models.CharField(choices=[('Call', 'Call'), ('Visitor', 'Visitor'), ('Email', 'Email'), ('Social Media', 'Social Media')], max_length=32)),
                ('lead_stage', models.CharField(choices=[('Initial Enquiry', 'Initial Enquiry'), ('Followup', 'Followup'), ('Closed', 'Closed')], max_length=32)),
                ('lead_action_took', models.CharField(choices=[('Informed Course Details', 'Informed Course Details'), ('Sent Syllabus', 'Sent Syllabus'), ('Sent Account Details', 'Sent Account Details'), ('Seat Pre-Booked', 'Seat Pre-Booked'), ('Seat Confirmed', 'Seat Confirmed')], max_length=64)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('mobile_number', models.CharField(max_length=10, unique=True)),
                ('mobile_number2', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('permanent_address', models.CharField(max_length=64)),
                ('current_address', models.CharField(max_length=64)),
                ('highest_qualification', models.CharField(choices=[('Masters', 'Masters'), ('Bachelors', 'Bachelors'), ('Diploma', 'Diploma'), ('12th', '12th'), ('10th', '10th'), ('School', 'School')], max_length=32)),
                ('stream', models.CharField(choices=[('Masters', 'Masters'), ('Bachelors', 'Bachelors'), ('Diploma', 'Diploma'), ('12th', '12th'), ('10th', '10th'), ('School', 'School')], max_length=32)),
                ('year_of_passing', models.CharField(choices=[('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025')], max_length=32)),
                ('type_of_course', models.CharField(choices=[('FullDay', 'FullDay'), ('Regular', 'Regular'), ('Weekend', 'Weekend')], max_length=32)),
                ('mode_of_course', models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=32)),
                ('course_interested', models.CharField(choices=[('Python', 'Python'), ('Java', 'Java'), ('C', 'C'), ('C++', 'C++'), ('Data Structures', 'Data Structures'), ('UI(FrontEnd)', 'UI(FrontEnd)')], max_length=32)),
                ('current_status_notes', models.CharField(max_length=64)),
            ],
        ),
    ]
