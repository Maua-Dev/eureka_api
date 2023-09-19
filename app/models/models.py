from django.db import models


class Paper(models.Model):
    assigment_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    shift = models.CharField(max_length=255)
    professor_id = models.IntegerField()
    stand_number = models.IntegerField()

    def to_dict(self):
        return {
            "assigment_id": self.assigment_id,
            "title": self.title,
            "shift": self.shift,
            "professor_id": self.professor_id,
            "stand_number": self.stand_number
        }

