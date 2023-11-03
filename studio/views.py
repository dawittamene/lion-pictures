from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .decorators import unauthenticated_user,allowed_users,admin_only
def index(request):
    return render(request, 'studio/index.html')
def about(request):
    return render(request, 'studio/about.html')

@login_required(login_url="loginpage")
def booking(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        mobile_number = request.POST['mobilenumber']
        email= request.POST['email']
        bookingdate = request.POST['bookingdate'] 
        bookingtime = request.POST['bookingtime']
        if Booking.objects.filter(Booking_Date=bookingdate).exists():
           return render(request,'studio/booking.html',{'booking_error':'A booking with the given date already exists.'})
        else:   
            new_booking = Booking(First_Name=first_name, Last_Name=last_name, Mobile=mobile_number, Email=email, Booking_Date=bookingdate, Time=bookingtime)
            new_booking.save()
            return redirect('Gallery')
    return render(request, 'studio/booking.html')

@login_required(login_url="loginpage")

def contact(request):
    if request.method == 'POST':
        name = request.POST['yourname']
        Email = request.POST['youremail']
        reason = request.POST['yourreason']
        Message = request.POST['yourmessage']
        new_contact = Contact(Name=name, email=Email, subject=reason, message=Message)
        new_contact.save()
        return redirect('booking')
    return render(request, 'studio/contact.html')

def Gallery(request):
    gallarys= Gallary_Post.objects.all()

    

    
    
    context = {'gallarys':gallarys}
    return render(request, 'studio/Gallery.html', context)   
@admin_only
def contact_booking(request):
    booking = Booking.objects.all()
    
    context ={'booking':booking}
    return render(request, 'admin/contact_booking.html', context)   
@admin_only
def messagess(request):
    contact = Contact.objects.all()
    context ={'contact':contact}
    return render(request, 'admin/messages.html', context) 

def findpage(request):
    if request.method == 'POST':
        user_id = request.POST.get('search')
        images=Image.objects.filter(user_id=user_id)
        context ={'images':images}
       
            

        return render(request, 'studio/picturs.html',context)
    return render(request, 'studio/find.html') 
@login_required(login_url="loginpage")
@admin_only
def post_user_photo(request):
    
    if request.method == 'POST':
        id = request.POST.get('user_id')
        imagesss = request.FILES.get('imagess')
        new_pic = Image.objects.create(user_id=id)
        new_pic.image=imagesss
        new_pic.save()
        # print(new_pic.image.url)
        return redirect('post_user_photo')
    return render(request, 'admin/post_user_photo.html') 

@unauthenticated_user
def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('booking')
        else:
            messages.success(request, "username or password is incorrect")
    context ={}
    return render(request, 'studio/login.html', context)

@unauthenticated_user
def signuppage(request):
    form=CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'account created successfully for ' + user)
            return redirect('loginpage')
        
    
        
    context ={'form':form}
    return render(request, 'studio/signup.html', context)
def logoutPage(request):
    logout(request)
    return redirect('loginpage')

@admin_only
def gallary_post(request):
    if request.method == 'POST':
        for_h1 = request.POST.get('for_h1_tag')
        for_text = request.POST.get('for_text_tag')
        
        imagesss = request.FILES.get('imagess')
        new_pic = Gallary_Post.objects.create(text_h1=for_h1,text_p=for_text)
        new_pic.gallary_post_image=imagesss
        new_pic.save()
        # print(new_pic.image.url)
        return redirect('gallary_post')
   
    return render(request, 'admin/gallary_post.html') 

def UpdatePage(request,pk):
    postform=PostForm()
    context ={'postform':postform}
    return render(request, 'admin/gallary_post.html', context) 
    
          



    

