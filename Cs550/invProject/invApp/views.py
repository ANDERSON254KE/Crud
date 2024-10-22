from django.shortcuts import render,get_object_or_404,redirect
from .forms import ProductForm
from .models import Products
#This is a CRUD application

# Create your views here.
# Home View
def home_view(request):
               return render(request,'invApp/home.html')
# Create view
def create_view(request):
        form=ProductForm()
        if request.method=='POST':
            form=ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('invApp:listings')
                
        return render(request,'invApp/product_form.html',context={'form':form})
# read View
def product_list_view(request):
        products=Products.objects.all()
        return render(request,'invApp/listings.html',context={'products':products})
# Update view
def update_view(request,product_id):  
        product=Products.objects.get(product_id=product_id)
        form=ProductForm(instance=product)

        if request.method=='POST':
                ProductForm()

                if form.is_valid():
                       form.save()
                return redirect('listings')
        return render(request,'invApp/product_form.html',context={'form':form})
        
# Delete View  
def delete_view(request, product_id):
    product = get_object_or_404(Products, product_id=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('invApp:listings')

    return render(request, 'invApp/delete.html', {'product': product})  # Redirect to the listings page if the request method is not POST
