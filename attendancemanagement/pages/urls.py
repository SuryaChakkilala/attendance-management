from django.urls import path
from .views import home, room_view, attendance1, attendance2, attendance3, attendance4, loginPage, logoutUser

urlpatterns = [
    path('', home, name='home'),
    path('room/<room_no>', room_view, name='room-view'),
    path('room/<room_no>/attendance1', attendance1, name='attendance1'),
    path('room/<room_no>/attendance2', attendance2, name='attendance2'),
    path('room/<room_no>/attendance3', attendance3, name='attendance3'),
    path('room/<room_no>/attendance4', attendance4, name='attendance4'),
    path('login', loginPage, name='login'),
    path('logout', logoutUser, name='logout')
]
