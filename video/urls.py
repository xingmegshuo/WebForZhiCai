from django.urls import path, re_path
from .views import home_view, login, video

urlpatterns = [
    path('', home_view),
    path('login', login),
    re_path(r'^(\d+)/$', video),
]
