from django.db import models

import uuid
# Create your models here.


class Problem(models.Model):

    LEVEL = (
        ("beginner", "beginner"),
        ("medium", "medium"),
        ("difficult", "difficult"),
    )

    LANGUAGE = (
        ("python", "python"),
        ("javasprits", "javasprits"),
        ("C++", "C++"),
    )

    TITLE = (
        ("Say hello with python", "Say hello with python"),
        ("Arithmetic Operators - Sum", "Arithmetic Operators - Sum"),
        ("Loops", "Loops"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100, choices=TITLE)
    problem = models.TextField()
    point = models.PositiveSmallIntegerField()
    level = models.CharField(max_length=50, choices=LEVEL)
    language = models.CharField(max_length=50, choices=LANGUAGE)
    input = models.CharField(max_length=100, blank=True)
    expected_output = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title 