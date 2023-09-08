from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Todo(models.Model):
    title = models.CharField("タスク名", max_length=30)
    description = models.TextField("詳細", blank=True)
    deadlineyear = models.IntegerField("締切年",validators=[MinValueValidator(2023), MaxValueValidator(2030)],null = True)
    deadlinemonth = models.IntegerField("締切月",validators=[MinValueValidator(1), MaxValueValidator(12)],null = True)
    deadlineday = models.IntegerField("締切日",validators=[MinValueValidator(1), MaxValueValidator(31)],null = True)
    importance = models.IntegerField("重みづけ",validators=[MinValueValidator(1), MaxValueValidator(5)],null = True)

    def __str__(self):
        return self.title

