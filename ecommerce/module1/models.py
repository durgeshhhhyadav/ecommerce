from django.db import models


# Create your models here.

class LoginData(models.Model):
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)
	email    = models.EmailField(max_length=255)
	mobileno = models.CharField(max_length=255)
	password = models.CharField(max_length=10)
	gender = models.CharField(max_length=10)
	role = models.CharField(max_length=20)
	date = models.CharField(max_length=20)
	time = models.CharField(max_length=20)

	class Meta():
		db_table = "login"

class AddProduct(models.Model):
	name = models.CharField(max_length=255)
	image1 = models.ImageField(upload_to='profile_pic', blank=True)
	image2 = models.ImageField(upload_to='profile_pic', blank=True)
	image3 = models.ImageField(upload_to='profile_pic', blank=True)
	category = models.CharField(max_length=255)
	price = models.CharField(max_length=255)
	
	date = models.CharField(max_length=20)
	time = models.CharField(max_length=20)
	class Meta():
		db_table = "product"

class SubProduct(models.Model):
	linkProductid = models.CharField(max_length=20)
	
	
	color = models.CharField(max_length=20)
	size = models.CharField(max_length=20)
	price = models.CharField(max_length=255)
	quantity = models.CharField(max_length=20)
	discount = models.CharField(max_length=20)
	


	date = models.CharField(max_length=20)
	time = models.CharField(max_length=20)
	updatedate = models.CharField(max_length=20)
	updatetime = models.CharField(max_length=20)
	class Meta():
		db_table = "subproduct"


class AddToCart(models.Model):
	userid = models.CharField(max_length=255)
	productid = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	image1 = models.CharField(max_length=255) 
	image2 = models.CharField(max_length=255)
	image3 = models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	size = models.CharField(max_length=255)
	color = models.CharField(max_length=255)
	price = models.CharField(max_length=255)
	quantity = models.CharField(max_length=255)
	quantityprice = models.CharField(max_length=255)
	discount = models.CharField(max_length=20)
	date = models.CharField(max_length=20)
	time = models.CharField(max_length=20)

	class Meta():
		db_table = "cart"


class ProductOrdered(models.Model):
	userid = models.CharField(max_length=255)
	productid = models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	size = models.CharField(max_length=255)
	color = models.CharField(max_length=255)
	discount = models.CharField(max_length=20)
	price = models.CharField(max_length=255)
	quantity = models.CharField(max_length=255)
	quantityprice= models.CharField(max_length=255)
	
	date = models.CharField(max_length=20)
	time = models.CharField(max_length=20)

	class Meta():
		db_table = "productordered"



class CustomerAddress(models.Model):
	linkUserid = models.CharField(max_length=50)
	address = models.CharField(max_length=255)
	country = models.CharField(max_length=255)
	state = models.CharField(max_length=255) 
	city = models.CharField(max_length=255)
	postcode = models.CharField(max_length=255)
	deliverycharged = models.CharField(max_length=255)
	total = models.CharField(max_length=255)

	date = models.CharField(max_length=20)
	time = models.CharField(max_length=20)


	class Meta():
		db_table = "customeraddress"



class ProductHistory(models.Model):
	userid = models.CharField(max_length=255)
	productid = models.CharField(max_length=255)
	size = models.CharField(max_length=255)
	color = models.CharField(max_length=255)
	discount = models.CharField(max_length=20)
	price = models.CharField(max_length=255)
	quantity = models.CharField(max_length=255)
	quantityprice = models.CharField(max_length=255)
	
	date = models.CharField(max_length=20)
	time = models.CharField(max_length=20)

	class Meta():
		db_table = "history"

