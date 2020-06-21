from django.db import models
from django.contrib.auth.models import User

class Nofication(models.Model):
    nof_date = models.DateTimeField('Дата')
    #nof_username = models.CharField('Имя пользователя', max_length=200,blank=True)
    #nof_email = models.CharField('Email', max_length=250,blank=True)
    nof_text = models.TextField('Уведомление')
    nof_user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Пользователь',default=None)
    class Meta():
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'

class Post(models.Model):
    post_name = models.CharField('post name',max_length=200)
    post_text = models.TextField('post text')
    post_pubdate = models.DateTimeField('publicate data')

    def __str__(self):
        return self.post_name
    class Meta():
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    about = models.TextField(blank=True)

class Curse(models.Model):
    curse_name = models.CharField('Название курса',max_length=200)
    curse_descr = models.TextField('Описание')
    curse_cost = models.IntegerField('Цена',default=0)
    curse_id = models.IntegerField('ID(посмотри ID последнего курса и напиши следущее число(ЭТО ВАЖНО))', default=0)
    curse_img = models.ImageField('Картинка',default=None,upload_to='images/')
    def __str__(self):
        return self.curse_name
    class Meta():
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

class CurseBuy(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey(Curse, on_delete=models.CASCADE)
    def __str__(self):
        return self.buyer.username
    class Meta():
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

class Lesson(models.Model):
    curse = models.ForeignKey(Curse, on_delete=models.DO_NOTHING,verbose_name='Для курса...')
    les_id = models.IntegerField('ID(посмотри ID последнего курса и напиши следущее число(ЭТО ВАЖНО))', default=1)
    les_title = models.CharField('Название урока',max_length=200)
    les_descr = models.TextField('Описание',blank=True)
    les_youtubelink = models.CharField('Youtube ссылка',max_length=250,blank=True)
    les_googlelink = models.CharField('Google disk ссылка', max_length=250,blank=True)
    def __str__(self):
        return self.les_title
    class Meta():
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

class Comment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,verbose_name='Урок')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Коментатор')
    com_text = models.TextField('Текст коментария')
    datetime = models.DateTimeField('Дата')
    comment_id = models.IntegerField('ID', default=0)
    def __str__(self):
        return str(self.commenter) + ': ' + str(self.com_text)

class CommentReply(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,verbose_name='Урок')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Коментатор')
    pr_comment = models.ForeignKey(Comment, on_delete=models.CASCADE,verbose_name='Родитель ком.')
    com_text = models.TextField('Текст коментария')
    datetime = models.DateTimeField('Дата')
    def __str__(self):
        return str(self.commenter) + ': ' + str(self.com_text)

class CurseLanding(models.Model):
    parent = models.ForeignKey(Curse, on_delete=models.CASCADE)
    presimage = models.ImageField('Пресент картинка',default=None,upload_to='images/landing/',blank=True)
    maindescription = models.TextField('Втрое описание')
    class Meta():
        verbose_name = 'Лендинг'
        verbose_name_plural = 'Лендинги'

class CurseLandingAsk(models.Model):
    parent = models.ForeignKey(CurseLanding,on_delete=models.CASCADE)
    ask = models.TextField('Вопрос')
    answer = models.TextField('Ответ')
    class Meta():
        verbose_name = 'Вопрос ответ'
        verbose_name_plural = 'Вопрос ответ'