from django.db import models


class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE, )
    content = models.CharField()
    date = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {
            "delivery_id": self.delivery_id,
            "task": self.task,
            "project": self.project,
            "user": self.user,
            "content": self.content,
        }
