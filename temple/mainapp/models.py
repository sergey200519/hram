from django.db import models

# Create your models here.


class News(models.Model):
    short_title = models.CharField(verbose_name="краткое название", max_length=128)
    title = models.TextField(verbose_name="полное название", blank=True)
    short_image = models.ImageField(verbose_name="фото", upload_to='news_images', blank=True)
    text = models.TextField(verbose_name="текст", blank=True, null=True)
    date = models.CharField(verbose_name="дата", max_length=12, blank=True)

    def __str__(self):
        return f'{self.short_title}'

    class Meta:
        verbose_name_plural = "Новости"


class ImgNews(models.Model):
    image = models.ImageField(upload_to='news_images', verbose_name="фото", blank=True)
    category_news = models.ForeignKey(News, verbose_name="новость", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'Фото к "{self.category_news}"'

    class Meta:
        verbose_name_plural = "Фото к новостям"


class Timetable(models.Model):
    date = models.CharField(verbose_name="дата", max_length=50, blank=True)
    description = models.TextField(verbose_name="празник(необезательно)", blank=True)
    time = models.CharField(verbose_name="время службы", max_length=200, blank=True)
    person = models.CharField(verbose_name="священослужитель(необезательно)", max_length=200, blank=True)
    HOLIDAY_CHOICES = (
      ('Y', "Воскресный"),
      ('N', 'Не воскресный')
    )
    holiday = models.CharField(verbose_name="какой день", choices=HOLIDAY_CHOICES, max_length=50, blank=True)

    def __str__(self):
        return f"{self.date}-{self.time} {self.description} {self.person}"

    class Meta:
        verbose_name_plural = "Расписание"


class Settings(models.Model):
    month = models.CharField(verbose_name="месяц", max_length=128)
    abbot = models.CharField(verbose_name="настоятель", max_length=128)
    phone = models.CharField(verbose_name="телефон", max_length=128)
    email = models.EmailField(verbose_name="почта")

    def __str__(self):
        return f'{self.month} | {self.abbot} | {self.phone} | {self.email}'

    class Meta:
        verbose_name_plural = "Настройки"
