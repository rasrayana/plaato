from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    descriptions = models.TextField(
        verbose_name="Описание сайта"
    )
    logo = models.ImageField(
        upload_to="logo_image",
        verbose_name="Логотоип сайта"
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телейонный номер"
    )
    facebook = models.URLField(
        verbose_name="Ссылка на Facebook",
        blank=True,null=True
    )
    instagram = models.URLField(
        verbose_name="Ссылка на Instagram",
        blank=True,null = True
    )
    youtube = models.URLField(
        verbose_name="Ссылка на Youtube",
        blank=True,null=True
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Основные параметры",
        verbose_name_plural = "Основные параметры"
        
class Slide(models.Model):
    image = models.ImageField(
        upload_to="slide_image",
        verbose_name="Фотография для слайда"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название для слайда"
    )
    descriptions = models.TextField(
        verbose_name="Описание для слайда"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Слайд",
        verbose_name_plural = "Слайды"
        
class About(models.Model):
    descriptions = models.TextField(
        verbose_name="Описание о нас"
    )
    
    
    def __str__(self):
        return self.descriptions
    
    class Meta:
        verbose_name = "О нас",
        verbose_name_plural = "О нас"

class History(models.Model):
    image_1 = models.ImageField(
        upload_to="history_image_1",
        verbose_name = "Первая фотография"
    )
    image_2 = models.ImageField(
        upload_to="history_image_2",
        verbose_name = "Второя фотография"
    )
    descriptions = models.TextField(
        verbose_name="Описание истории"
    )
    
    def __str__(self):
        return self.descriptions
    
    class Meta:
        verbose_name = "Наша история",
        verbose_name_plural = "Наша история"
        
class Offer(models.Model):
    image = models.ImageField(
        upload_to="offer_image",
        verbose_name="Фотография"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название блюда"
    )
    descriptions = models.TextField(
        verbose_name="Описание блюда"
    )
    price = models.CharField(
        max_length=255,
        verbose_name="Цена"
    )
    type = models.CharField(
        max_length=255,
        verbose_name="Тип блюда"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Предложение",
        verbose_name_plural = "Предложение"