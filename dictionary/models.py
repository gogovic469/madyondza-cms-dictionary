from django.db import models

class Entry(models.Model):
    word = models.CharField(max_length=30)
    meaning = models.TextField()
    dialect = models.CharField(max_length=15)

    def __unicode__(self):
        return self.word