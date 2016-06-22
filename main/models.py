from django.db import models


class Chirp(models.Model):
    body = models.CharField(max_length=141)
    created = models.DateTimeField(auto_now_add=True)
    bird = models.ForeignKey("auth.User")

    class Meta:
        ordering = ["-created"]


class StopWord(models.Model):
    word = models.CharField(max_length=45)
