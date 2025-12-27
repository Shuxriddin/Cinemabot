from django.db import models
# Create your models here.
class BotUserModel(models.Model):
    languages = (
        ('uz', "O'zbek",),
        ('en', "English")
    )
    name = models.CharField(max_length=300,null=True,blank=True,verbose_name="Full Name",help_text="Enter full name")
    telegram_id = models.CharField(max_length=100,unique=True,verbose_name="Telegram ID",help_text="Enter telegram id")
    language = models.CharField(max_length=5,default='uz',choices=languages,verbose_name="Language",help_text="Choose language")
    added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        if self.name:
            return f"{self.name}"
        else:
            return f"User with ID:{self.telegram_id}"
    class Meta:
        verbose_name = 'Bot User'
        verbose_name_plural='Bot Users'
class TelegramChannelModel(models.Model):
    channel_id = models.CharField(max_length=150,verbose_name="Channel ID",help_text="Enter channel id",unique=True)
    channel_name = models.CharField(max_length=300,verbose_name="Channel Name",help_text="Enter channel name",null=True,blank=True)
    channel_members_count = models.CharField(max_length=200,null=True,blank=True,verbose_name="Channel Memers Count",help_text="Enter channel members count")
    def __str__(self):
        return f"Channel: {self.channel_id}"
    class Meta:
        verbose_name = 'Telegram Channel'
        verbose_name_plural = 'Telegram Channels'


# ==========================================

class Movie(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    file_id = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255, unique=True, null=True, blank=True)
    is_series = models.BooleanField(default=False)
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title if self.title else self.id}"

    class Meta:
        verbose_name = 'Kino'
        verbose_name_plural = 'Kinolar'

class Episode(models.Model):
    movie = models.ForeignKey(Movie, related_name='episodes', on_delete=models.CASCADE)
    file_id = models.CharField(max_length=255)
    number = models.IntegerField()
    code = models.CharField(max_length=255, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie.title} - {self.number}-qism"

    class Meta:
        verbose_name = 'Qism'
        verbose_name_plural = 'Qismlar'
        ordering = ['number']
