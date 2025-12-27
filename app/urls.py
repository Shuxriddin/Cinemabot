from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('botuser', BotUserViewset)
router.register('channels', TelegramChannelViewset)
router.register('movies', MoviesViewset)
router.register('episodes', EpisodeViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('user/', GetUser.as_view()),
    path('lang/', ChangeUserLanguage.as_view()),
    path('channel/', GetTelegramChannel.as_view()),
    path('delete_channel/', DeleteTelegramChannel.as_view()),
    path('movie/', CreateMovieView.as_view()),
    path('movie_code/<int:id>', SearchMovieCodeView.as_view(), name='movie_code'),  # This should be correct
    path('movie/<int:id>/', GetFilmView.as_view()),
    path('movie_rate/<int:id>/', MovieRateView.as_view(), name='movie_rate'),
    path('movie_top/', TopMoviesView.as_view())
]
