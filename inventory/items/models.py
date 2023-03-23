from django.db import models


class Inventory(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название оборудования',
        unique=True
    )
    title = models.TextField(
        verbose_name='Полное название',
        blank=True
    )
    serial = models.CharField(
        max_length=100,
        verbose_name='Инвентарный номер',
        blank=True,
        db_index=True
    )
    create_at = models.DateField(
        verbose_name='Дата постановки на учет',
        auto_now=True
    )
    update_at = models.DateField(
        verbose_name='Дата смены владельца',
        auto_now=True
    )
    first_name_owner = models.CharField(
        verbose_name='Имя владельца',
        max_length=20,
        null=True
    )
    middle_name_owner = models.CharField(
        verbose_name='Отчество владельца',
        max_length=20,
        null=True
    )
    last_name_owner = models.CharField(
        verbose_name='Фамилия владельца',
        max_length=20,
        null=True
    )
    room = models.CharField(
        verbose_name='Местонахождение оборудования',
        max_length=30,
        null=True
    )

    def __str__(self):
        return f'{self.name}-{self.serial}-{self.last_name_owner}-{self.room}'

