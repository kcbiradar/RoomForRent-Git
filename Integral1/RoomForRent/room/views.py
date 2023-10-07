from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm

from .forms import RegisterUserForm,RoomForm,RentedForm,QueriesForm

from django.http import HttpResponse

from .models import Room,Cities,RentedRooms

from django.db.models import Q

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,"Wrong Credentials...")
            return redirect('login')

    else:
        return render(request, 'room/login.htm')


def logout_user(request):
    logout(request)
    return redirect('home')   


def home(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    #order = RentedRooms.objects.all()
    room_list = Room.objects.filter(city__icontains=q).exclude(Q(id__in=RentedRooms.objects.values('room_id')))
    order = RentedRooms.objects.all()
    return render(request, 'room/home.htm',{
        'room_list':room_list,
        'order': order
        })

@login_required(login_url='login')
def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.owner = request.user
            room.save()
            return redirect('home')
    return render(request, 'room/create_room.htm',{'form':form})

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            messages.success(request,'Registration successful')
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request, 'room/login_register.htm',{'form':form})


def all_cities(request):
    cities = Cities.objects.all()
    return render(request, 'room/cities.htm',{'cities':cities})

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.owner:
        return HttpResponse('You are not allowed alter details of this room')
    
    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request,'room/create_room.htm',context) 


def booking(request,pk):
    rooms = Room.objects.get(id=pk)
    form = RentedForm(request.POST,instance=rooms)
    if request.method == 'POST':
        form = RentedForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.buyer_username = request.user
            room.room_id_id = pk
            
            room.save()
            
            return redirect('home')
    context = {'rooms':rooms,'form':form}
    return render(request,'room/room.htm',context)

@login_required(login_url='login')
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.user != room.owner:
        return HttpResponse('You are not allowed remove this room')
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'room/delete.htm',{'room':room})


def contact_us(request):
    form = QueriesForm()
    if request.method == 'POST':
        form = QueriesForm(request.POST)
        if form.is_valid():
            query = form.save(commit=False)
            query.username = request.user
            query.save()
            return redirect('home')
    return render(request,'room/contact_us.htm',{'form':form})

@login_required(login_url='login')
def deleteRentedRooms(request):
    room = RentedRooms.objects.exclude(room_id__owner = request.user.id)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'room/cancel.htm',{'room':room})

def orderedRoom(request):
    order = RentedRooms.objects.all()
    return render(request,'room/order.htm',{'order':order})



def myRoomsBooked(request):
    my_rooms = RentedRooms.objects.filter(room_id__owner = request.user.id)
    print(my_rooms)
    return render(request , 'room/booked_rooms.htm' , {'my_rooms' : my_rooms})