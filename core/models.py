from django.db import models


class Message(models.Model):
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField()
    is_deleted = models.BooleanField()

    class Meta:
        db_table = "core_messages"

# class Message(models.Model):
#     sender = models.TextField()
#     receiver = models.TextField()
#     subject = models.TextField()
#     body = models.TextField()
#     created_at = models.DateTimeField()
#     is_deleted = models.BooleanField()

#     class Meta:
#         db_table = "core_messages"