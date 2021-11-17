from django.db import models

highest_qualification_choices = (
    ('Masters','Masters'),
    ('Bachelors','Bachelors'),
    ('Diploma','Diploma'),
    ('12th','12th'),
    ('10th','10th'),
    ('School','School'),
)

stream_choices = (
    ('Mechanical Engg.','Mechanical Engg.'),
    ('Civil Engg.','Civil Engg.'),
    ('Electrical Engg.','Electrical Engg.'),
    ('Electronics Engg.','Electronics Engg.'),
    ('Computer Engg.','Computer Engg.'),
    ('Information Technology','Information Technology'),
    ('Other','Other'),
)

year_of_passing_choices = (
    ('2000', '2000'),
    ('2001', '2001'),
    ('2002', '2002'),
    ('2003', '2003'),
    ('2004', '2004'),
    ('2005', '2005'),
    ('2006', '2006'),
    ('2007', '2007'),
    ('2008', '2008'),
    ('2009', '2009'),
    ('2010', '2010'),
    ('2011', '2011'),
    ('2012', '2012'),
    ('2013', '2013'),
    ('2014', '2014'),
    ('2015', '2015'),
    ('2016', '2016'),
    ('2017', '2017'),
    ('2018', '2018'),
    ('2019', '2019'),
    ('2020', '2020'),
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023'),
    ('2024', '2024'),
    ('2025', '2025'),
)

type_of_course_choices = (
    ('FullDay','FullDay'),
    ('Regular','Regular'),
    ('Weekend','Weekend'),
)

mode_of_course_choices = (
    ('Online','Online'),
    ('Offline','Offline'),
)
course_interested_choices = (
    ('Python','Python'),
    ('Java','Java'),
    ('C','C'),
    ('C++','C++'),
    ('Data Structures','Data Structures'),
    ('UI(FrontEnd)','UI(FrontEnd)'),
    ('Aptitude','Aptitude'),
    ('AWS(Cloud Computing)','AWS(Cloud Computing)'),
    ('Spoken English','Spoken English'),
)

type_of_lead_choices = (
    ('Call','Call'),
    ('Visitor','Visitor'),
    ('Email','Email'),
    ('Social Media','Social Media'),
)

lead_stage_choices = (
    ('Initial Enquiry','Initial Enquiry'),
    ('Followup','Followup'),
    ('Closed','Closed')
)

lead_action_took_choices = (
    ('Informed Course Details','Informed Course Details'),
    ('Sent Syllabus','Sent Syllabus'),
    ('Sent Account Details','Sent Account Details'),
    ('Seat Pre-Booked','Seat Pre-Booked'),
    ('Seat Confirmed','Seat Confirmed'),
)

# Create your models here.
class Lead(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    handled_by = models.CharField(max_length=32)
    type_of_lead = models.CharField(max_length=32, choices=type_of_lead_choices)
    lead_stage = models.CharField(max_length=32, choices=lead_stage_choices)
    lead_action_took = models.CharField(max_length=64, choices=lead_action_took_choices)
    #
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32,blank=True)
    mobile_number = models.CharField(max_length=10,unique=True)
    mobile_number2 = models.CharField(max_length=10,blank=True)
    email = models.EmailField(blank=True)
    referred_by = models.CharField(max_length=32,blank=True)
    permanent_address = models.CharField(max_length=64)
    current_address = models.CharField(max_length=64)
    highest_qualification = models.CharField(max_length=32,choices=highest_qualification_choices)
    stream = models.CharField(max_length=32,choices=stream_choices)
    school_college = models.CharField(max_length=64)
    year_of_passing = models.CharField(max_length=32,choices=year_of_passing_choices)
    type_of_course = models.CharField(max_length=32,choices=type_of_course_choices)
    mode_of_course = models.CharField(max_length=32,choices=mode_of_course_choices)
    course_interested = models.CharField(max_length=32,choices=course_interested_choices)
    current_status_notes = models.CharField(max_length=128)



