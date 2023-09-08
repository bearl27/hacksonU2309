from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Todo(models.Model):
    title = models.CharField("タスク名", max_length=30)
    description = models.TextField("詳細", blank=True)
    deadline = models.DateField("締切",null = True, blank = True)
    importance = models.IntegerField("重みづけ",validators=[MinValueValidator(1), MaxValueValidator(5)],null = True)

    def __str__(self):
        return self.title

