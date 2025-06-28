from django.shortcuts import render,redirect
from Fend.models import logdb,regdb,contactdb,cartdb
from Bend.models import catdb,prodb
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):

    data=catdb.objects.all()
    da=prodb.objects.all()
    return render(request,"home.html",{'data':data,'da':da})

def discategory(request,itemCatg):
    data = catdb.objects.all()
    print("===itemCatg===",itemCatg)
    catg=itemCatg.upper()
    products=prodb.objects.filter(category=itemCatg)
    context={
        'products':products,
        'catg':catg,
        'data':data
    }
    return render(request,"discategory.html",context)
def products(request):
    data = catdb.objects.all()
    da = prodb.objects.all()
    return render(request,"products.html",{'da':da,'data':data})
def prodetails(request,dataid):
    data = prodb.objects.get(id=dataid)
    da=catdb.objects.all()
    return render(request,"prodetails.html",{'data':data,'da':da})
def contact(request):
    data= catdb.objects.all()
    return render(request,"contact.html",{'data':data})
def reglog(request):
    data = catdb.objects.all()
    return render(request,"reglog.html",{'data':data})
def logdata(request):
    if 'username' in request.session:
        return redirect(home)
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        User = authenticate(username=username,password=password)

        if User is not None:
            login(request,User)
            request.session['username'] = username
            request.session['password'] = password
            return redirect(home)
        else:
            return render(request,'reglog.html',{'mess':"sorry...Invalid username Or Password "})
def regdata(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email=request.POST.get("email")
        password = request.POST.get("password")
        password2=request.POST.get("password2")
        obj=regdb(username=username,email=email,password=password,password2=password2)
        obj.save()


        if password==password2:
            if User.objects.filter(username=username):
                return redirect(reglog)
            elif User.objects.filter(email=email):
                return redirect(reglog)
            else:
                user =User.objects.create_user(username=username,password=password,email=email)
                user.save()
                print('user created')
                return redirect(reglog)
        else:
            return render(request,'reglog.html',{'mess':"sorry...Invalid username Or Password "})
def logout(request):
    del request.session['username']
    return redirect(home)
def contactsave(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        msg=request.POST.get('msg')
        obj = contactdb(name=name, email=email,msg=msg)
        obj.save()
        return redirect(contact)
def cart(request):
    data=cartdb.objects.all()
    da=catdb.objects.all()
    return render(request,"cart.html",{'data':data,'da':da})
def prodetailsave(request):

    if request.method=="POST":
        image = request.FILES['img']
        name=request.POST.get('name')
        quantity=request.POST.get('qty')
        totalprice=request.POST.get('totalprice')
        size=request.POST.get('size')
        obj=cartdb(image=image,name=name,quantity=quantity,totalprice=totalprice,size=size)
        obj.save()
        return redirect(prodetails)