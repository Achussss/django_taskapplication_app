from django.db import models

# Create your models here.


class  Tasks(models.Model):
    task_name=models.CharField(max_length=200)
    created_date=models.DateField(auto_now_add=True)
    status=models.BooleanField(default=False)
    user=models.CharField(max_length=200)
    

    def _str_(self):
        return self.task_name
