from django.db import models


class Quote(models.Model):

    author = models.CharField(max_length=50, default='')
    text = models.CharField(max_length=255)
    posted_date = models.DateTimeField('date published')

    def __str__(self):
        return "<id>" + str(self.id) + " <text> " + self.text + " <Author> " + self.author + " <posted_date> " + self.posted_date.strftime("%Y-%m-%d %H:%M:%S")