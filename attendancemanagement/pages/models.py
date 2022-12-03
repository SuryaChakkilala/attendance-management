from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

room_list = [
    ('C107', 'C107'),
    ('C108', 'C108'),
    ('C109', 'C109'),
    ('C110', 'C110'),
    ('C111', 'C111'),
    ('C121', 'C121'),
    ('C225', 'C225'),
    ('C307', 'C307'),
    ('C308', 'C308'),
    ('C309', 'C309'),
    ('C321B1', 'C321B1'),
    ('C321B2', 'C321B2'),
    ('C325', 'C325'),
    ('C406', 'C406'),
    ('C407', 'C407'),
    ('C410', 'C410'),
    ('C411', 'C411'),
    ('C421A', 'C421A'),
    ('C422', 'C422'),
    ('C423', 'C423'),
    ('C425', 'C425'),
    ('C525', 'C525'),
    ('C625', 'C625'),
    ('GroundFloorLab', 'GroundFloorLab'),
    ('FirstFloorLab', 'FirstFloorLab'),
    ('SecondFloorLab', 'SecondFloorLab'),
    ('ThirdFloorLab', 'ThirdFloorLab'),
    ('FourthFloorLab', 'FourthFloorLab'),
    ('SixthFloorLab', 'SixthFloorLab')
    ]

class Team(models.Model):
    team_no = models.CharField(max_length=250)
    business_system = models.CharField(max_length=255)
    room_no = models.CharField(choices=room_list, max_length=255)

    def __str__(self):
        return str(self.team_no) + '_' + self.business_system


class Student(models.Model):
    cat_choice = (
        (2, 2),
        (3, 3),
    )
    reg_no = models.CharField(max_length=10)
    name = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(choices=cat_choice)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    attendance_1 = models.BooleanField(default=False)
    attendance_2 = models.BooleanField(default=False)
    attendance_3 = models.BooleanField(default=False)
    attendance_4 = models.BooleanField(default=False)

    def __str__(self):
        return self.reg_no
    

    