from django.contrib import admin

# Register your models here.
from .models import BotUserModel,TelegramChannelModel, Movie
@admin.register(BotUserModel)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ['name','telegram_id','language','added']
    list_editable = ['language','name']
    list_display_links = ['telegram_id']
    list_per_page = 10
@admin.register(TelegramChannelModel)
class TelegramChannelAdmin(admin.ModelAdmin):
    list_display = ['channel_id','channel_name','channel_members_count']
    list_display_links = ['channel_name']
    list_per_page = 10

@admin.register(Movie)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['description','file_id']
    list_display_links = ['file_id']
    list_per_page = 10
