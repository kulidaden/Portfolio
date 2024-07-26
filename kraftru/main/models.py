from django.db import models
from django.core.validators import MinValueValidator


class Task(models.Model):
    title=models.CharField("Ім'я та фамілія", max_length=50)
    number=models.IntegerField("Номер телефону",validators=[MinValueValidator(1)])
    task_choice = [(0, 'Ландшафтний дизайн'), (1, 'Клінінг'), (2, 'Облаштування інтер\'єру'), (3, 'Охоронна система'), (4, 'Дизайн інтер\'єру')]
    task = models.IntegerField(choices=task_choice)



    def __str__(self):
        return f'{self.title} {self.number} {self.task}'

    class Meta:
        verbose_name='Задача'
        verbose_name_plural='Задачи'