from django.db import models

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=120, blank=True, default='')
    code = models.TextField()
    user = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
