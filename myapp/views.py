from django.shortcuts import render,redirect
from .forms import signupForm,notesForm
from .models import usersignup,mynotes
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import send_mail
from BatchProject import settings
import random

# Create your views here.

def index(request):
    if request.method=='POST':  #root
        # Signup
        if request.POST.get('signup')=='signup':
            username=''
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                username=newuser.cleaned_data.get('emailid')
                try:
                    un=usersignup.objects.get(emailid=username)
                    print('\nEmail Address already in use.\n')
                    messages.warning(request,'Email Address already in use.')
                except:
                    newuser.save()
                    print("\nUser created successfully!\n")
                    messages.success(request,'User created successfully!')

                    #Email Sending Code
                    """fnm=request.POST['fname']
                    lnm=request.POST['lname']
                    sub='Welcome!'
                    msg=f'Hello, {fnm} {lnm}!\nNotesApp welcomes you. We hope you will enjoy our services.'
                    to_ID=[request.POST['emailid']]
                    send_mail(subject=sub,message=msg,from_email=settings.EMAIL_HOST_USER,recipient_list=to_ID)"""

                    # OTP verification
                    """otp = random.randint(100000,999999)
                    sub ='Welcome!'
                    msg =f'Your verification code is {otp}.'
                    url = "https://www.fast2sms.com/dev/bulkV2"
                    querystring = {"authorization":"YOUR API KEY","message":f'{msg}',"language":"english","route":"q","numbers":"10 DIGIT PHONE NUMBER"}
                    headers = {
                    'cache-control': "no-cache"
                    }
                    response = requests.request("GET", url, headers=headers, params=querystring)
                    print(response.text)"""

                    return redirect('/')
            else:
                print(newuser.errors)
        # Login
        elif request.POST.get('login')=='login':
            emid=request.POST['emailid']
            pas=request.POST['pwd']
            
            Login_check=usersignup.objects.filter(emailid=emid,pwd=pas) #check user login credentials
            
            uid=usersignup.objects.get(emailid=emid) # get user id

            if Login_check:
                print('\nLogin successful!!\n')
                request.session['user']=emid
                request.session['userid']=uid.id
                return redirect('notes')
            else:
                print('Error! Email or password is incorrect.')
                messages.error(request,'Error! Email or password is incorrect.')
    return render(request,'index.html')

def notes(request):
    user=request.session.get('user')
    uid=request.session.get('userid')
    cuser=usersignup.objects.get(id=uid)
    if request.method=='POST':
        mynote=notesForm(request.POST,request.FILES)
        if mynote.is_valid():
            # loginuser=signupForm(request.POST,instance=cuser)
            mynote.save()
            print('\nYour query has been posted.\n')
            messages.info(request,'Your query has been posted.')
        else:
            print(mynote.errors)
    return render(request,'notes.html',{'user':user,'cuser':usersignup.objects.get(id=uid)})

def updateprofile(request):
    user=request.session.get('user')
    uid=request.session.get('userid')
    cuser=usersignup.objects.get(id=uid)
    if request.method=='POST':
        updateuser=signupForm(request.POST)
        if updateuser.is_valid():
            updateuser=signupForm(request.POST,instance=cuser)
            updateuser.save()
            print('\nYour profile has been updated.\n')
            messages.success(request,'Your profile has been updated')
            return redirect('updateprofile')
        else:
            print(updateuser.errors)
    return render(request,'updateprofile.html',{'user':user,'cuser':usersignup.objects.get(id=uid)})

def userlogout(request):
    logout(request)
    return redirect('/')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')