from django.db import models


class Paper(models.Model):
    assigment_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    shift = models.CharField(max_length=255)
    professor_id = models.IntegerField()
    stand_number = models.IntegerField()

    def __str__(self):
        return self.title


