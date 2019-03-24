from django.utils import timezone
from django.db import models
from database.models import User


class Chat(models.Model):
    DIALOG = 'D'
    CHAT = 'C'
    CHAT_TYPE_CHOICES = (
        (DIALOG, 'Dialog'),
        (CHAT, 'Chat')
    )

    type = models.CharField(
        'Тип',
        max_length=1,
        choices=CHAT_TYPE_CHOICES,
        default=DIALOG
    )
    members = models.ManyToManyField(User, verbose_name="Участник")

    def get_absolute_url(self):
        return 'users:messages', (), {'chat_id': self.pk}


class Message(models.Model):
    chat = models.ForeignKey(Chat, verbose_name="Чат", on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    message = models.TextField("Сообщение")
    pub_date = models.DateTimeField('Дата сообщения', default=timezone.now())
    is_readed = models.BooleanField('Прочитано', default=False)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.message
