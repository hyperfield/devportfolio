from django.db import models


class Update(models.Model):
    title = models.CharField(max_length=127)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    update = models.ForeignKey('Update', on_delete=models.CASCADE,
                               related_name='comments')

    def __str__(self):
        return f"""{self.author}, on
               {self.created_on.strftime('%Y-%m-%d @ %H:%M:%S')}"""
