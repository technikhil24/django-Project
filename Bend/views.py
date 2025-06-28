from django.shortcuts import render,redirect
from Bend.models import empdb,catdb,prodb,logdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from Fend.models import regdb,contactdb
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


# Create your views here.
def login(request):
    return render(request,"login.html")
def logsave(request):
    if 'name' in request.session:
        return redirect(index)
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        User = authenticate(username=username, password=password)

        if User is not None:
            login(request)
            request.session['name'] = username
            request.session['password'] = password
            return redirect(index)
        else:
            return render(request, 'login.html', {'mess': "sorry...Invalid username Or Password "})
def signout(request):
    del request.session['name']
    del request.session['password']
    return redirect(login)

def index(request):
    data = contactdb.objects.all()
    return render(request,"index.html",{'data':data})
def empadd(request):
    return render(request,"employeeadd.html")
def empsave(request):
    if request.method=="POST":
        name=request.POST.get('name')
        adrs=request.POST.get('adrs')
        mob=request.POST.get('mob')
        email=request.POST.get('email')
        image=request.FILES['image']
        obj = empdb(name=name, adrs=adrs, mob=mob, email=email, image=image)
        obj.save()
        return redirect(empadd)



def empdetails(request):
    data=empdb.objects.all()
    return render(request,"employeedetails.html",{'data':data})
def empedit(request,dataid):
    data=empdb.objects.get(id=dataid)
    print(data)
    return render(request,"employeeEdit.html",{'data':data})
def updatedata(request,dataid):
    if request.method=="POST":
        name = request.POST.get('name')
        adrs = request.POST.get('adrs')
        mob = request.POST.get('mob')
        email = request.POST.get('email')
        try:
            image = request.FILES['image']
            fs = FileSystemStorage()
            file= fs.save(image.name.image)
        except MultiValueDictKeyError:
            file =empdb.objects.get(id=dataid).image
        empdb.objects.filter(id=dataid).update(name=name,adrs=adrs,mob=mob,email=email,image=file)
        return redirect(empdetails)
def empdelete(request,dataid):
    data=empdb.objects.filter(id=dataid)
    data.delete()
    return redirect(empdetails)
def catadd(request):
    return render(request,"categoryadd.html")
def catsave(request):
    if request.method=="POST":
        cname= request.POST.get('cname')
        price= request.POST.get('price')
        image = request.FILES['image']
        obj = catdb(cname=cname, price=price, image=image)
        obj.save()
        return redirect(catadd)

def catdetails(request):
    data=catdb.objects.all()
    return render(request,"categorydetails.html",{'data':data})
def catedit(request,dataid):
    data=catdb.objects.get(id=dataid)
    print(data)
    return render(request,"categoryEdit.html",{'data':data})
def catupdate(request,dataid):
    if request.method=="POST":
        cname = request.POST.get('cname')
        price = request.POST.get('price')
        try:
            image = request.FILES['image']
            fs = FileSystemStorage()
            file= fs.save(image.name.image)
        except MultiValueDictKeyError:
            file =catdb.objects.get(id=dataid).image
        catdb.objects.filter(id=dataid).update(cname=cname,price=price,image=file)
        return redirect(catdetails)
def catdelete(request,dataid):
    data=catdb.objects.filter(id=dataid)
    data.delete()
    return redirect(catdetails)
def proadd(request):
    data = catdb.objects.all()
    return render(request,"productadd.html",{'data':data})
def prosave(request):
    if request.method == "POST":
        category = request.POST.get('category')
        name= request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES['image']
        obj = prodb(category=category,name=name, price=price, image=image)
        obj.save()
        return redirect(proadd)
def prodetails(request):
    data = prodb.objects.all()
    return render(request, "productdetails.html", {'data': data})
def proedit(request,dataid):
    da=catdb.objects.all()
    data = prodb.objects.get(id=dataid)
    print(data)
    return render(request, "productEdit.html", {'data': data,'da':da})
def proupdate(request,dataid):
    if request.method=="POST":
        category = request.POST.get('category')
        name = request.POST.get('name')
        price = request.POST.get('price')
        try:
            image = request.FILES['image']
            fs = FileSystemStorage()
            file= fs.save(image.name.image)
        except MultiValueDictKeyError:
            file =prodb.objects.get(id=dataid).image
            prodb.objects.filter(id=dataid).update(category=category,name=name,price=price,image=file)
        return redirect(prodetails)
def prodelete(request,dataid):
    data = prodb.objects.filter(id=dataid)
    data.delete()
    return redirect(prodetails)
def regdetails(request):
    data=regdb.objects.all()
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        obj = regdb(username=username, email=email, password=password, password2=password2)
        obj.save()
    return render(request,"registerdetails.html",{'data':data})
def contactdetails(request):
    data=contactdb.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        obj = contactdb(name=name, email=email, msg=msg)
        obj.save()
    return render(request,"contactdetails.html",{'data':data})
def contactdlt(request,dataid):
    data=contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(contactdetails)

