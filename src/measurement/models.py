from django.db import models


class Sensor(models.Model):
    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    name = models.CharField(max_length=100, verbose_name='Название датчика')
    description = models.TextField(blank=True, verbose_name='Описание датчика')


class Measurement(models.Model):
    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'

    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name='Идентификатор датчика', related_name='measurements')
    temperature = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Значение температуры')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время измерения')
