from django.shortcuts import render,redirect
from products.models import Product
from accounts.models import Cart,CartItems
from django.http import HttpResponseRedirect
# from products.models import SizeVariant,ColorVariant


# Create your views here.
def get_product(request , slug):
    try:
        product = Product.objects.get(slug =slug)
        return render(request  , 'product/product.html' , context = {'product' : product})

    except Exception as e:
        print(e)

def add_to_cart(request,uid):
    user=request.user
    product=Product.objects.get(uid=uid)
    cart,_ = Cart.objects.get_or_create(user=user,is_paid=False)
    cart_item=CartItems.objects.create(cart=cart,products=product)
    # variant=request.GET.get("variant")
    # if variant:
    #     size_variant=SizeVariant.objects.get(size_name=variant)
    #     cart_item.size_variant=size_variant
    #     cart_item.save()
    return render(request,"accounts/cart.html")
    # return HttpResponseRedirect(request.path_info)