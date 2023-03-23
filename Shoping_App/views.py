from django.shortcuts import redirect, render

from Shoping_App.models import customer

# Create your views here.
def Shoping_App (request):
    return render(request, "index.html", {})

def about (request):
    return render (request, "about.html", {})

def blog (request):
    return render (request, "blog.html", {})

def blogimg(request):
    return render (request, "blogimg.html", {})

def blogvid (request):
    return render (request, "blogvid.html", {})

def blogaud (request):
    return render (request, "blogaud.html", {})

def blogfull1 (request):
    return render (request, "blogfull1.html", {})

def blogfull2 (request):
    return render (request, "blogfull2.html", {})

def blogleft (request):
    return render (request, "blogleft.html", {})

def blogleft2 (request):
    return render (request, "blogleft2.html", {})

def blogright (request):
    return render(request, "blogright.html", {})

def cart (request):
    return render(request, "cart.html", {})

def checkout (request):
    return render(request, "checkout.html", {})

def compare(request):
    return render (request, "compare.html", {})

def contactus (request):
    return render (request, "contactus.html", {})

def index2 (request):
    return render (request, "index2.html", {})

def index3 (request):
    return render(request, "index3.html", {})

def index4 (request):
    return render(request, "index4.html", {})

def loginreg (request):
    return render (request, "loginreg.html", {})

def myaccount (request):
    return render (request, "myaccount.html", {})

def paffilate (request):
    return render (request, "paffilate.html", {})

def pbox (request):
    return render (request, "pbox.html", {})

def pdetailsgroup (request):
    return render (request, "pdetailsgroup.html", {})

def pdetailsvar (request):
    return render (request, "pdetailsvar.html", {})

def productdetails (request):
    return render (request, "productdetails.html", {})

def shopgrid3 (request):
    return render(request, "shopgrid3.html", {})

def shopgrid4 (request):
    return render(request, "shopgrid4.html", {})

def shopgridleft (request):
    return render (request, "shopgridleft.html", {})

def shopgridleft3 (request):
    return render (request, "shopgridleft3.html", {})

def shopgridright (request):
    return render (request, "shopgridright.html", {})

def shopgridright3 (request):
    return render (request, "shopgridright3.html", {})

def shoplistfull (request):
    return render (request, "shoplistfull.html", {})

def shoplistleft (request):
    return render (request, "shoplistleft.html", {})

def shoplistright (request):
    return render (request, "shoplistright.html", {})

def singleprodgroup (request):
    return render (request, "singleprodgroup.html", {})

def singleproduct (request):
    return render(request, "singleproduct.html", {})

def singleprosale (request):
    return render (request, "singleprosale.html", {})

def wishlist (request):
    return render (request, "wishlist.html", {})

def signin(request):
    return render (request, "signin.html", {})

def register (request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        country = request.POST.get('country')
        password = request.POST.get('password')
        
        

        #Let's create a NEw customer object
        customer = customer(firstname=firstname, lastname=lastname, email=email,country=country, password = password, address = address)
        customer.save()

        return redirect('loginreg')
    return render (request, 'loginreg.html')

def login(request):
    if request.method == 'POST':
        #Get Data from HTML Form
        email = request.POST.get('email')
        password = request.POST.get('password')

        #LET'S AUTHENTICATE CUSTOMERS 
        customer.customer.object.filer(email=email, password=password) .first()
        if customer is not None:
            return redirect ('myaccount')
        
        else:
            return render(request, 'loginreg.html', {'error': 'Invalid email or password'})
        return render(request, 'loginreg.html')
    

       








