from rest_framework.serializers import ModelSerializer
from .models import BotUserModel, TelegramChannelModel, Movie, Episode
class BotUserSerializer(ModelSerializer):
    class Meta:
        model = BotUserModel
        fields = '__all__'
class TelegramChannelSerializer(ModelSerializer):
    class Meta:
        model = TelegramChannelModel
        fields = '__all__'

class EpisodeSerializer(ModelSerializer):
    class Meta:
        model = Episode
        fields = ['id', 'number', 'file_id', 'code', 'created_at']

class MovieSerializer(ModelSerializer):
    episodes = EpisodeSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
