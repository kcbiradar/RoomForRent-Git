from django.contrib import admin

from .models import Room,RentedRooms,Cities,Queries

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ['id','owner','city','address','price','contact_details','room_type']
    class Meta:
        model = Room

class QueriesAdmin(admin.ModelAdmin):
    list_display = ['username','room_id','email','problem']
    class Meta:
        model = Queries
# class OwnerAdmin(admin.ModelAdmin):
#     list_display = ['username','name','room_Id']
#     class Meta:
#         model = Owner

class RentedRoomsAdmin(admin.ModelAdmin):
    list_display = ['id','room_id', 'buyer_username']
    class Meta:
        model = RentedRooms

# admin.site.register(Owner,OwnerAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(RentedRooms,RentedRoomsAdmin)
admin.site.register(Queries,QueriesAdmin)
admin.site.register(Cities)
               