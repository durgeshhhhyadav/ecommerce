from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from module1.models import LoginData,AddProduct,AddToCart,ProductOrdered,ProductHistory,CustomerAddress,SubProduct
from module1.forms import LoginForm,SignupForm,AddProductForm,SubProductForm
from .import forms
import json
#from django.shortcuts import redirect

# Create your views here.

count=0
count1=0
count2=0
count3=0
count4=0
total = 0
deliverycharged=""

count5=0


def autocompleteModel(request):
    if request.method=="POST":
        q = request.GET.get('term', '').capitalize()
        search_qs = AddProduct.objects.filter(name=q)
        results = []
        print(q)
        for r in search_qs:
            results.append(r.FIELD)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)





def about(request):
	global count
	print(count)
	cartitem=0
	p = AddToCart.objects.all()
	if count == 0:

		cartitem=0
	if count == 1:
		for i in p:
			if int(request.session['userid']) == int(i.userid):
				cartitem+=1
	return render(request, 'about.html',{'cartitem' : cartitem})

def blogdetail(request):
	global count
	print(count)
	cartitem=0
	p = AddToCart.objects.all()
	if count == 0:

		cartitem=0
	if count == 1:
		for i in p:
			if int(request.session['userid']) == int(i.userid):
				cartitem+=1
	return render(request, 'blog-detail.html',{'cartitem' : cartitem})

def blog(request):
	global count
	print(count)
	cartitem=0
	p = AddToCart.objects.all()
	if count == 0:

		cartitem=0
	if count == 1:
		for i in p:
			if int(request.session['userid']) == int(i.userid):
				cartitem+=1
	return render(request,'blog.html',{'cartitem' : cartitem})

def contact(request):
	global count
	print(count)
	cartitem=0
	p = AddToCart.objects.all()
	if count == 0:

		cartitem=0
	if count == 1:
		for i in p:
			if int(request.session['userid']) == int(i.userid):
				cartitem+=1
	return render(request,'contact.html',{'cartitem' : cartitem})

def index(request):
	global count
	print(count)
	cartitem=0
	p = AddToCart.objects.all()
	if count == 0:

		cartitem=0
	if count == 1:
		for i in p:
			if int(request.session['userid']) == int(i.userid):
				cartitem+=1

	s3=SubProduct.objects.all()
	s1=AddProduct.objects.all()
	paginator = Paginator(s1,10)
	page = request.GET.get('page')
	s2 = paginator.get_page(page)

	return render(request, 'index.html',{'data' : s2,'data1' : s1,'data2':s3,'cartitem' : cartitem})
	#return render(request,'index.html',{'data' : range(10),'gotodiv' : 'go'})

def home02(request):
	return render(request,'home-02.html')

def productdetail(request,myid):
	global count
	global count1
	global count2
	count2 = myid
	cartitem=0
	check=1
	p = AddToCart.objects.all()
	if count == 0:
		cartitem=0
	if count == 1:
		for i in p:
			if int(request.session['userid']) == int(i.userid):
				cartitem+=1
	s1=AddProduct.objects.all()
	paginator = Paginator(s1,4)
	page = request.GET.get('page')
	s2 = paginator.get_page(page)
	p = AddProduct.objects.get(id=myid)
	#p1 = AddToCart.objects.all()
	'''for i in p1:
		print(i.id)
		print(i.userid)
		print(i.productid)
		if int(i.userid) == int(request.session['userid']) and int(i.productid) == int(myid):
			count1=1
			print("count"+str(count1))'''


	return render(request, 'product-detail.html',{'product' : p,'data' : s2,'data1' : s1,'cartitem' : cartitem, 'check': check})


def updatecolorsize(request,myid,cartid):
	global count
	global count1
	global count2
	global count4

	count2 = myid
	cartitem=0
	check=1
	cart = cartid
	p3 = AddToCart.objects.get(id=cartid)
	updatecolor=p3.color
	updatesize=p3.size

	p2 = AddToCart.objects.all()

	count4 = 1

	if count == 0:
		cartitem=0
	if count == 1:
		for i in p2:
			if int(request.session['userid']) == int(i.userid):
				cartitem+=1
	s1=AddProduct.objects.all()
	paginator = Paginator(s1,4)
	page = request.GET.get('page')
	s2 = paginator.get_page(page)
	p1 = AddProduct.objects.get(id=myid)
	#p3 = AddToCart.objects.all()
	'''for i in p3:
		print(i.id)
		print(i.userid)
		print(i.productid)
		if int(i.userid) == int(request.session['userid']) and int(i.productid) == int(myid):
			count1=1
			print("count"+str(count1))'''


	return render(request, 'product-updatecolorsize.html',
							{'product' : p1,'data' : s2,
							'data1' : s1,'cartitem' : cartitem,
							 'checkcart' : count1, 'check': check,
							 'cartid' : cart,'p3':p3,
							 'black' : "black",'blue' : "blue"})


def addtocart(request,myid):
	global count
	global count1
	global count2
	print("addtocart")
	
	cartitem=0
	check=1
	a=0
	d=0
	try:
		p = AddToCart.objects.all()
		if count == 0:
			cartitem=0
		if count == 1:
			for i in p:
				if int(request.session['userid']) == int(i.userid):
					cartitem+=1
	except Exception as e:
		pass
	

	
	if count == 1 :
		print("ifaddto cart")
		if request.method == "POST":
			size1 = request.POST['size']
			color1 = request.POST['color']
			

					
			p1 = AddToCart.objects.all()
			print("addtocart1")
			p4 = AddProduct.objects.get(id=myid)
			print("addtocart2")
			for i in p1:
				print(i.id)
				print(i.userid)
				print(i.productid)
				print(i.size)
				print("size1"+size1)
				print(i.color)
				print("color1"+color1)
				if int(i.userid) == int(request.session['userid']) and int(i.productid) == int(myid) and str(size1) == str(i.size) and str(color1) == str(i.color):
					count1=1
					count3=1
					print("count"+str(count1))

		
		if count1==0:
			if request.method == "POST":
				size = request.POST['size']
				color = request.POST['color']
				quantity = request.POST['quantity']

				p2 = AddProduct.objects.get(id=myid)

				p5 = SubProduct.objects.all()
				print("p5")
				for j in p5:
					print("start")
					print(j.linkProductid)
					print(p2.id)
					print(j.size)
					print(size)
					print(j.color)
					print(color)
					if int(j.linkProductid) == int(p2.id) and j.size == size and j.color == color and j.quantity>=quantity:
						a=j.price
						d=j.discount

				
				if a==0 and d==0:
					s1=AddProduct.objects.all()
					paginator = Paginator(s1,4)
					page = request.GET.get('page')
					s2 = paginator.get_page(page)
					p3 = AddProduct.objects.get(id=myid)
					p1 = AddToCart.objects.all()
					s3 = "This size and color are not available...."
					count1=0
					return render(request,"product-detail.html",{'product': p3, 'cartitem' : cartitem, 'data' : s2,'data1' : s1,'s1' : s3 })
					#return HttpResponseRedirect('module1/productdetail/%d'%myid)


				else:
					quantityprice = int(quantity)*int(a)

					userid = request.session['userid']
					current_time = datetime.now()
					date1="%s-%s-%s" %(current_time.day, current_time.month, current_time.year)
					time1="%s:%s" %(current_time.hour, current_time.minute)
					shopingcart = AddToCart(userid=userid,
											 productid=p2.id,
											name = p2.name,
											image1 = p2.image1,
											image2 = p2.image2,
											image3 = p2.image3,
											category = p2.category,
											size = size,
											color = color,
											price = p2.price,
											quantity= quantity,
											quantityprice= quantityprice,
											discount=d,
											date = date1,
											time = time1)

					shopingcart.save()
					return redirect("/module1/shopingcart")




		elif count1==1:
			s1=AddProduct.objects.all()
			paginator = Paginator(s1,4)
			page = request.GET.get('page')
			s2 = paginator.get_page(page)
			p3 = AddProduct.objects.get(id=myid)
			p1 = AddToCart.objects.all()
			s3 = "This is already added...."
			count1=0
			return render(request,"product-detail.html",{'product': p3, 'cartitem' : cartitem, 'data' : s2,'data1' : s1,'s1' : s3 })
			#return HttpResponseRedirect('module1/productdetail/%d'%myid)
	return redirect('/module1/login')


def updateshopingcart(request,myid):
	global count
	global count1
	global count2
	global count4
	
	count1=0
	cartitem=0
	check=1
	'''p = AddToCart.objects.all()
	if count == 0:
		cartitem=0
	if count == 1:
		for i in p:
			if int(request.session['userid']) == int(i.userid):
				cartitem+=1'''

	
	
	if count == 1 :
		if count4==1:
			if count1==0:
				if request.method == "POST":

					size = request.POST['size']
					color = request.POST['color']
					quantity = request.POST['quantity']

					p = AddProduct.objects.get(id=myid)

					quantityprice = int(quantity)*int(p.price)
					userid = request.session['userid']
					current_time = datetime.now()
					date1="%s-%s-%s" %(current_time.day, current_time.month, current_time.year)
					time1="%s:%s" %(current_time.hour, current_time.minute)

					p2 = AddToCart.objects.filter(id=request.POST['acartid'])

					p2.update(size = size,color = color,price = p.price,quantity= quantity,quantityprice= quantityprice)
	
					return redirect("/module1/shopingcart")
			elif count1==1:
				s1=AddProduct.objects.all()
				paginator = Paginator(s1,4)
				page = request.GET.get('page')
				s2 = paginator.get_page(page)
				p3 = AddProduct.objects.get(id=count3)
				p1 = AddToCart.objects.all()
				s3 = "This is already added...."
				return render(request,"product-detail.html",{'product': p3, 'data' : s2,'data1' : s1,'s1' : s3 })
				#return HttpResponseRedirect('module1/productdetail/%d'%myid)
	return redirect('/module1/login')

def shopingcart(request):
	global count
	global total
	global deliverycharged
	localcount = 0
	total = 0
	deliverycount=999
	deliverycharged =""
	if count == 0:
		p=None



	
	if count == 1:
		p1=SubProduct.objects.all()
		p = AddToCart.objects.all()
		a=0

		for i in p:
			if int(request.session['userid'])== int(i.userid):
				a+=int(i.quantityprice)

		if a>999 or a==0:
			deliverycharged ="Free"
			total=a
		else:
			deliverycharged=149
			total=a+int(deliverycharged)

		

	return render(request,'shoping-cart.html',{'products' : p,'products1':p1,'subtotal': a,'total': total,'deliverycharged':deliverycharged,'deliverycount' :deliverycount })


def removecart(request,myid):
	if(myid):
		p = AddToCart.objects.get(id=myid)
		p.delete()

		
	return redirect('/module1/shopingcart')



def product(request):
	global count
	print(count)
	cartitem=0
	p = AddToCart.objects.all()
	if count == 0:

		cartitem=0
	if count == 1:
		for i in p:
			if int(request.session['userid']) == int(i.userid):
				cartitem+=1
	s1=AddProduct.objects.all()
	paginator = Paginator(s1,8)
	page = request.GET.get('page')
	s2 = paginator.get_page(page)
	return render(request, 'product.html',{'data' : s2,'data1' : s1,'cartitem' : cartitem})

def login(request):
	global count
	l = forms.LoginForm()
	print("entry")
	if request.method == "POST":
		print("POST")
		username = request.POST['username']
		password = request.POST['password']

		try:
			p = LoginData.objects.get(email=username, password=password)
		except Exception as e:
			messages.success(request, 'userid and password are not metch!')
			return redirect("/module1/login")
			
		
		if username == p.email and password == p.password and p.role == "user":
			a=p.firstname
			b=p.id
			print(b)
			request.session['username'] = a
			request.session['userid'] = b
			print(request.session['userid'])
			count = 1
			return redirect("/module1/index")
		elif username == p.email and password == p.password and p.role == "admin":
			a=p.firstname
			b=p.id
			request.session['username'] = a
			request.session['userid'] = b
			count = 1
			return redirect("/module1/adminshowproduct")
			

			
	else:
		return render(request, 'login.html',{ 'data' : l})

def logout(request):
	global count
	for key in request.session.keys():
		print(key)

	print(request.session['username'])
	print(request.session['userid'])
	if request.session.has_key('username') and request.session.has_key('userid') :
		request.session.flush()
		count = 0
		return redirect('/module1/index')


'''def submitform(request):
	sessionVar = "NO user"
	if request.method == "POST": 
		f = forms.LoginForm(request.POST)
		if f.is_valid():
			name = f.cleaned_data['user_name']
			print(name)

			request.session['sessionVar'] = name
			return render(request, 'index.html', {'data' : request.session['sessionVar'] })

		return render(request, 'login.html', {'data' : sessionVar })'''


def signup(request):
	l = forms.SignupForm()
	form = SignupForm(request.POST)

	if form.is_valid():
		current_time = datetime.now()
		date1="%s-%s-%s" %(current_time.day, current_time.month, current_time.year)
		time1="%s:%s" %(current_time.hour, current_time.minute)
		signup = LoginData(firstname = form.cleaned_data['firstname'],
						lastname = form.cleaned_data['lastname'],
						email    = form.cleaned_data['email'],
						mobileno = form.cleaned_data['mobileno'],
						password = form.cleaned_data['password'],
						gender = form.cleaned_data['gender'],
						role = "user",
						date = date1,
						time = time1)
		if form.cleaned_data['password'] == form.cleaned_data['repassword']:
			signup.save()
			return redirect('/module1/login')
			

	else:
		return render(request, 'signup.html',{'data' : l})

'''def submit(request):
	sessionVar = "NO user"
	if request.method == "POST": 
		f = forms.SignupForm(request.POST)
		if f.is_valid():
			name = f.cleaned_data['firstname']
			print(name)

			request.session['sessionVar'] = name
			return render(request, 'login.html', {'data1' : request.session['sessionVar'] })

		return render(request, 'signup.html', {'data1' : sessionVar })'''


def addproduct(request):
	global count3
	localcount=0
	l = forms.AddProductForm()
	form = AddProductForm(request.POST)

	try:
		if request.session['userid'] != '': 
			if form.is_valid():
				current_time = datetime.now()
				date1="%s-%s-%s" %(current_time.day, current_time.month, current_time.year)
				time1="%s:%s" %(current_time.hour, current_time.minute)
				addproduct = AddProduct(name = form.cleaned_data['name'],
									image1 = form.cleaned_data['image1'],
									image2 = form.cleaned_data['image2'],
									image3 = form.cleaned_data['image3'],
									category = form.cleaned_data['category'],
									price= form.cleaned_data['price'],
									date = date1,
									time = time1,)
				addproduct.save()

				
				return redirect('/module1/subproduct')
			else:
				return render(request, 'addproduct.html',{'data' : l})
	except Exception as e:
		return redirect('/module1/index')
#########################################################################################################################################
def subproduct(request):
	global count5
	localcount=0
	l = forms.SubProductForm()
	proid =AddProduct.objects.latest('id')
	count5 = proid.id
	form = SubProductForm(request.POST)

	try:
		if request.session['userid'] != '':
			print("1")
			if form.is_valid():
				color=form.cleaned_data['color']
				size = form.cleaned_data['size']
				subprice = form.cleaned_data['price']

				p5 = SubProduct.objects.all()
				print("p5")
				for j in p5:
					print("start")
					print(j.linkProductid)
					print(j.size)
					print(size)
					print(j.color)
					print(color)
					if int(j.linkProductid) == int(proid.id) and j.size == size and j.color == color:
						localcount=1


				if localcount==1:
					s3 = "This detail already exist...."
					return render(request,"sub-addproduct.html",{'data' : l, 's1' : s3 })
					#return HttpResponseRedirect('module1/productdetail/%d'%myid)
				elif int(subprice) == int(proid.price):
					s3 = "please enter price"+str(proid.price)
					return render(request,"sub-addproduct.html",{'data' : l, 's1' : s3 })
				else:
					print("2")
					current_time = datetime.now()
					date1="%s-%s-%s" %(current_time.day, current_time.month, current_time.year)
					time1="%s:%s" %(current_time.hour, current_time.minute)
					print("3")
					subproduct = SubProduct(linkProductid = proid.id,
										color = form.cleaned_data['color'],
										size = form.cleaned_data['size'],
										price = form.cleaned_data['price'],
										quantity = form.cleaned_data['quantity'],
										discount = form.cleaned_data['discount'],
										date = date1,
										time = time1,
										updatedate = date1,
										updatetime = time1)
					subproduct.save()

				
				return redirect('/module1/subproduct')
			else:
				return render(request, 'sub-addproduct.html',{'data' : l})
	except Exception as e:
		return redirect('/module1/index')

#########################################################################################################################


#########################################################################################################################


def updatesubproduct(request, id):
	global count5
	count5 = id
	try:
		if request.session['userid'] != '':
			p = AddProduct.objects.get(id=id)
			p1 = SubProduct.objects.all()
			'''for i in p1:
				if i.linkProductid == p.id:'''
				
			

			return render(request,'subproductshow.html',{'product': p,'product1' : p1})
	except Exception as e:
		return redirect('/module1/index')

def updatesubproduct1(request, id): #subproduct id
	global count5
	try:
		print("try")
		if request.session['userid'] != '':
			print("try2")
			p = SubProduct.objects.get(id=id)
			print("try3")
			'''for i in p1:
				if i.linkProductid == p.id:'''
				
			

			return render(request,'subproductedit.html',{'subproduct': p,'productid': count5 })
	except Exception as e:
		return redirect('/module1/index')

def subproductupdated(request):
	global count5
	if request.session['userid'] != '':
			p = AddProduct.objects.get(id=count5)
			p1 = SubProduct.objects.all()
			try:
				if request.session['userid'] != '':
					if request.method == "POST":
						color = request.POST['spcolor']
						size = request.POST['spsize']
						price = request.POST['spprice']
						quantity = request.POST['spquantity']
						discount = request.POST['spdiscount']
						p2 = SubProduct.objects.filter(id=request.POST['spid'])
						current_time = datetime.now()
						date="%s-%s-%s" %(current_time.day, current_time.month, current_time.year)
						time="%s:%s" %(current_time.hour, current_time.minute)
						p2.update(color=color, 
									size = size, 
									price = price, 
									quantity =quantity, 
									discount = discount,
									updatedate = date,
									updatetime = time)

						return render(request,'subproductshow.html',{'product': p,'product1' : p1})
					return redirect("/module1/adminshowproduct")
			except Exception as e:
				return redirect('/module1/index')

def subproductshow(request):
	global count5
	if request.session['userid'] != '':
			p = AddProduct.objects.get(id=count5)
			p1 = SubProduct.objects.all()

			return render(request,'subproductshow.html',{'product': p,'product1' : p1})

def addmore(request,myid):
	localvar=0
	print("try11")
	l = forms.SubProductForm()

	proid =AddProduct.objects.get(id=myid)

	form = SubProductForm(request.POST)

	
	p1 = SubProduct.objects.all()
	print("try22")
	try:
		if request.session['userid'] != '':
			print("1")
			if form.is_valid():
				print("2")
				current_time = datetime.now()
				date1="%s-%s-%s" %(current_time.day, current_time.month, current_time.year)
				time1="%s:%s" %(current_time.hour, current_time.minute)
				print("3")
				subproduct = SubProduct(linkProductid = proid.id,
									color = form.cleaned_data['color'],
									size = form.cleaned_data['size'],
									price = form.cleaned_data['price'],
									quantity = form.cleaned_data['quantity'],
									discount = form.cleaned_data['discount'],
									date = date1,
									time = time1,
									updatedate = date1,
									updatetime = time1)
				subproduct.save()

				
				return render(request,'subproductshow.html',{'product': proid,'product1' : p1})
			else:
				return render(request, 'sub-addproduct.html',{'data' : l})
	except Exception as e:
		return redirect('/module1/index')

################################################################################################################################################
def adminShowProduct(request):
	try:
		if request.session['userid'] != '':
			p1=AddProduct.objects.all()
			paginator = Paginator(p1,2)
			page = request.GET.get('page')
			p2 = paginator.get_page(page)
			return render(request,'adminshowproduct.html',{'data' : p2 , 'data1': p1})
	except Exception as e:
		return redirect('/module1/index')




def deletesubproduct(request, id):
	try:
		if request.session['userid'] != '':
			if(id):
				p = SubProduct.objects.get(id=id)
				p.delete()
				messages.success(request, 'Item has been deleted!')
				return redirect("/module1/subproductshow")
	except Exception as e:
		return redirect('/module1/index')



def adminProductDetail(request,id):
	try:
		if request.session['userid'] != '':
			p = AddProduct.objects.get(id=id)
			return render(request, 'adminproduct-detail.html',{'product' : p})
	except Exception as e:
		return redirect('/module1/index')



def orderproduct(request):
	global total
	global deliverycharged
	localcount = 0
	localcount1 = 0
	localcount2 = 0
	localcount3 = 0

	userid = request.session['userid']

	current_time = datetime.now()
	date1="%s-%s-%s" %(current_time.day, current_time.month, current_time.year)
	time1="%s:%s" %(current_time.hour, current_time.minute)

	try:	
		p1= AddToCart.objects.all()
		if request.method == "POST":
			for i in p1:
				if int(i.userid) == int(request.session['userid']):


					
					p3 = SubProduct.objects.all()
					for j in p3:
						if int(j.linkProductid) == int(i.productid) and str(j.color) == str(i.color) and str(j.size) == str(i.size):
							localcount2=1
							if int(j.quantity) >= int(i.quantity) and int(j.quantity)>0:
								pass
							else:
								localcount1=1
								break
						
							


					
				
			if localcount1 == 0:
				p2= AddToCart.objects.all()
				for k in p2:
					if int(k.userid) == int(request.session['userid']):
						productorder=ProductOrdered(userid = k.userid ,
													productid = k.productid,
													category =k.category ,
													size = k.size,
													color = k.color,
													discount = k.discount,
													price = k.price,
													quantity = k.quantity,
													quantityprice= k.quantityprice,
									
													date = date1,
													time = time1,)

						p4 = SubProduct.objects.all()
						for l in p4:
							if int(l.linkProductid) == int(k.productid) and str(l.color) == str(k.color) and str(l.size) == str(k.size):
								if int(l.quantity) >= int(k.quantity) and int(l.quantity)>0:
									quantity=int(l.quantity)-int(k.quantity)

									p5 = SubProduct.objects.filter(id=l.id)

									p5.update(quantity= quantity)
	

									productorder.save()
									p = AddToCart.objects.get(id=k.id)
									p.delete()

									localcount=1

			else:
				messages.success(request, 'please remove your outofstock products from cart..!')
				return redirect('/module1/shopingcart')


			if localcount==1:
				address = request.POST['address']
				country = request.POST['country']
				state = request.POST['state']
				city = request.POST['city']
				postcode = request.POST['postcode']
				#deliverycharged =request.POST['deliverycharge']
				customeraddress=CustomerAddress(
										linkUserid = userid,
										address =address,
										country = country,
										state = state,
										city = city,
										postcode = postcode,
										deliverycharged = deliverycharged,
										total = total,
										date = date1,
										time = time1,)
				customeraddress.save()
				total= 0
				return redirect('/module1/index')

				'''p3=ProductOrdered.objects.all()
				for i in p3:
					if int(i.userid) == int(request.session['userid']):
						a1= i.productid
						i.color
						i.size
						i.quantity
						p4 = AddProduct.objects.get(id=a1)
						p4 = AddProduct.objects.filter(id=a1)
						for i in p4:

						i.quantity'''


			if localcount2 == 0:
				messages.success(request, "your cart don't have any product")
				return redirect('/module1/shopingcart')
	except Exception as e:
		messages.success(request, "your cart don't have any product")
		return redirect('/module1/shopingcart')
		

	


def showorder(request):
	products=CustomerAddress.objects.all()
	return render(request,'show-order.html',{'orders' : products})


def showorderdetails(request,myid,iid):#myid is a userid
	print("showorderdetails11")
	user = LoginData.objects.get(id=int(myid))
	print("showorderdetails1")
	customer=CustomerAddress.objects.get(id=int(iid))
	print("showorderdetails2")

	products1=CustomerAddress.objects.all()

	products=ProductOrdered.objects.all()


	return render(request,'order-details.html',{'details' : products,'details1': products1,'user':user,'customer':customer})
