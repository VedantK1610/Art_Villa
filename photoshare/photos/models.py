from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    title=models.CharField(max_length=100,default="title")
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    image=models.ImageField(null=False,blank=False)
    description=models.TextField()
    selling_price=models.FloatField()
    artist_name=models.CharField(max_length=100,default='SOME STRING')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
     user_name=models.CharField(max_length=100,null=False)  
     user_comment=models.TextField()  

     def __str__(self):
         return self.user_comment   

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    is_verified=models.BooleanField(default=False)

    def __str__(self) :
        return self.user.username
    

class urequesr(models.Model):
    username=models.CharField(max_length=100)
    msg=models.CharField(max_length=500)
    insta=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True,auto_created=True)
    artistname=models.CharField(max_length=100,default="Any Artist")

    def __str__(self) :
        return self.username
    
class artistname(models.Model):
     username=models.CharField(max_length=100,null=False) 


     def __str__(self):
         return self.username   
    
# class Cart(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     product=models.ForeignKey(Photo,on_delete=models.CASCADE)
#     quantity=models.PositiveIntegerField(default=1)

#     @property
#     def total_cost(self):
#         return self.quantity * self.product.selling_price    

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=200,null=True)
    razor_pay_order_id=models.CharField(max_length=100,null=True,blank=True)
    razor_pay_payment_id=models.CharField(max_length=100,null=True,blank=True)
    razor_pay_payment_signature=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total
    
    @property
    def shipping(self):
        shipping=True
        return shipping
    
class OrderItem(models.Model):
    product=models.ForeignKey(Photo,on_delete=models.SET_NULL,blank=True,null=True)    
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total=self.product.selling_price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=200,null=True)
    zipcode=models.CharField(max_length=200,null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address