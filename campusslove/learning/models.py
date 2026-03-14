from django.db import models

class LearningMaterial(models.Model):
    user_id = models.IntegerField()
    
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)

    notes = models.TextField(blank=True) # for writting notes

    link = models.URLField(blank=True)

    file = models.FileField(upload_to='learning_files/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
