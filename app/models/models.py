from django.db import models


class Paper(models.Model):
    paper_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    shift = models.CharField(max_length=255)
    professors = models.ManyToManyField('Professor')
    stand_number = models.CharField(max_length=255)

    

    def to_dict(self):
        return {
            "paper_id": self.paper_id,
            "title": self.title,
            "shift": self.shift,
            "stand_number": self.stand_number,
            "professors": [professor.to_dict() for professor in self.professors.all()]
        }


class Professor(models.Model):
    professor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    rf = models.CharField(max_length=255)
    
    def to_dict(self):
        return {
            "professor_id": self.professor_id,
            "name": self.name,
            "rf": self.rf
        }

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ra = models.CharField(max_length=255)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, default=None, null=True)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "ra": self.ra,
            "paper": self.paper.to_dict()
        }
