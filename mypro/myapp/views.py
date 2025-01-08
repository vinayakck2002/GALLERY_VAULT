from django.shortcuts import render,redirect
from . models import Gallery
from django.contrib.auth import authenticate, login, logout as authlogout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def signin(request):
    if request.user.is_authenticated:
        return redirect(viewsmain)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,password)
        # Check if both fields are provided
        if not username or not password:
            messages.error(request, "Both username and password are required!")
            return render(request, 'index.html')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            request.session['username'] = user.username
            request.session['user_id'] = user.id
            return redirect(index)  # Redirect to the home page after login
        else:
            messages.error(request, "Invalid credentials")
    
    return render(request, 'index.html')

def index(request):
    return render(request,'index3.html')

def usersignup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        # print(email,username,password,confirmpassword)
        if password==confirmpassword:
            User.objects.create_user(username=username, email=email, password=password)
            return redirect("signin")
    return render(request, "index2.html")


# ---------------------------------------------gallery vault page--------------------------------------------------------------------------  # 
def viewsmain(request):
    # user=User.objects.get(user=request.session['username'])
    # if request.method == "POST":
    #     imgdef = request.FILES['files']  # Get the uploaded file from the request
    #     # print(imgdef)  # You can remove this print statement after testing
        
    #     # Create and save a new ImgForm object with the uploaded image
    #     obj = Gallery(classimages=imgdef,User=request.user)
    #     obj.save()
    #     return redirect(viewsmain)  # Redirect to the index view to refresh the page

    # # Fetch all ImgForm objects to display the images
    # imagefeeds = Gallery.objects.all()
    # return render(request, "index3.html", {"feeds": imagefeeds})

    #-------------------------------------------chatgpt--------------------------------------------------
    if not request.user.is_authenticated:
        return redirect('signin')  # Redirect to sign-in if not authenticated
    
    if request.method == "POST":
        imgdef = request.FILES['files']  # Get the uploaded file from the request
        
        # Create and save a new Gallery object with the uploaded image
        obj = Gallery(classimages=imgdef, User=request.user)  # Save the image for the logged-in user
        obj.save()
        return redirect(viewsmain)  # Redirect to refresh the page

    # Fetch only the images uploaded by the logged-in user
    imagefeeds = Gallery.objects.filter(User=request.user)  # Filter images by the current user
    return render(request, "index3.html", {"feeds": imagefeeds})

def delete(request,pk):
    imagefeeds=Gallery.objects.get(pk=pk)
    imagefeeds.delete()
    return redirect(viewsmain)

def add(request):
    return render(request,'imgadd.html')

def picture(request,id):
    imagefeeds=Gallery.objects.get(pk=id)
    feeds = imagefeeds.classimages.url
    return render(request,'images.html',{"feeds":feeds})
def images(request,pk):
    img=Gallery.objects.get(pk=pk)





def logout(request):
    if 'username' in request.session:
        del request.session['username']
    if 'user_id' in request.session:
        del request.session['user_id']
    authlogout(request)
    return redirect('../')





