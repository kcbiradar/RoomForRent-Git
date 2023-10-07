from django.urls import path

from .import views

urlpatterns = [ 
    path('',views.home, name='home'),
    path('create-room/',views.create_room, name='create-room'),
    path('register/',views.register_user, name='register'),
    path('login_user/',views.login_user, name='login'),
    path('logout_user/',views.logout_user, name='logout'),
    path('cities/',views.all_cities, name='cities'),
    path('update-room/<int:pk>/',views.updateRoom, name='update-room'),
    path('room/<int:pk>/',views.booking, name='room'),
    path('delete/<int:pk>/',views.deleteRoom, name='delete'),
    path('contact-us',views.contact_us, name='contact-us'),
    path('cancel/',views.deleteRentedRooms, name='cancel'),
    path('order/',views.orderedRoom, name='order'),
    path('my_rooms/',views.myRoomsBooked, name='my_rooms'),
]