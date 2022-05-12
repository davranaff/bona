from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return f'name: {self.name}'

class Product(models.Model):
	COUNTRY_CHOICES = (
		('UZ' , 'UZBEKISTAN'),
		('RU' , 'RUSSIA'),
		('AZE' , 'AZERBAIJAN'),
		('TURK' , 'TURKEY'),
		('UAE' , 'UAE'),
		('UKR' , 'UKRAINE'),
		('IRAN' , 'IRAN'),
	)
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='images/')
	description = models.TextField(null = True)
	price = models.FloatField()
	quantity = models.FloatField()
	discounted_product = models.BooleanField(default=False, blank=True, null=True)
	discounted_price = models.IntegerField(blank=True, null=True)
	product_category = models.ForeignKey(Category, on_delete= models.CASCADE)
	country = models.CharField(max_length=100,choices = COUNTRY_CHOICES)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'product: {self.name}  , quantity : {self.quantity}'


class Basket(models.Model):
	owner = models.ForeignKey(User, on_delete = models.CASCADE)
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	quantity = models.FloatField()

	def __str__(self):
		return f'owner : {self.owner}'

	def total_price(self):
		return self.product.price * self.quantity


class Order(models.Model):
	address = models.CharField(max_length=255)
	email = models.EmailField(max_length=254)
	telephone_number = models.CharField(max_length=255)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	buy = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return f'owner : {self.owner} '





class OrderProduct(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_product')
	amount = models.FloatField(default=0)
	total = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f'owner : {self.order.owner} |product: {self.product} |total {self.amount} kg \ ltr |price {self.total} AED'


class Slider(models.Model):
	image = models.ImageField(upload_to='slider/')
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True , blank=True)
	description = models.CharField(max_length=255 , null=True , blank=True)

	def __str__(self):
		return f"slider"

class BuyLater(models.Model):
	quantity = models.FloatField()
	date = models.DateTimeField()
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE , null=True)

	def __str__(self):
		return f'owner : {self.owner}'

	def total_price(self):
		return self.product.price * self.quantity