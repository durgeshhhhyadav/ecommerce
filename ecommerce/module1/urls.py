from django.urls import path
from  .import views

urlpatterns=[
		path('about',views.about, name="about"),
		path('blogdetail', views.blogdetail, name="blogdetail"),
		path('blog', views.blog, name="blog"),
		path('contact', views.contact, name="contact"),
		path('index', views.index, name="index"),
		path('home02', views.home02, name="home02"),
		path('productdetail/<int:myid>', views.productdetail, name="productdetail"),

		path('addtocart/<int:myid>', views.addtocart, name="addtocart"),
		path('shopingcart', views.shopingcart, name="shopingcart"),
		path('removecart/<int:myid>', views.removecart, name="removecart"),


		path('product', views.product, name="product"),
		path('login', views.login, name="login"),
		path('logout', views.logout, name="logout"),
		path('signup', views.signup, name="signup"),

		path('addproduct', views.addproduct, name="addproduct"),
		path('subproduct', views.subproduct, name="subproduct"),
		
		
		path('updatesubproduct/<int:id>', views.updatesubproduct, name="updateproduct"), # productid 
		path('updatesubproduct1/<int:id>', views.updatesubproduct1, name="updateproduct1"), # subproductid
		path('subproductupdated', views.subproductupdated, name="subproductupdated"),
		path('subproductshow', views.subproductshow, name="subproductshow"),
		path('addmore/<int:myid>', views.addmore, name="addmore"),

		path('deletesubproduct/<int:id>', views.deletesubproduct, name="deletesubproduct"),
		path('adminshowproduct', views.adminShowProduct, name="adminShowProduct"),
		path('showorder', views.showorder, name="showorder"),
		path('showorderdetails/<int:myid>/<int:iid>', views.showorderdetails, name="showorderdetails"),

		path('adminproductdetail/<int:id>', views.adminProductDetail, name="adminProductDetail"),
		#path('updatecart', views.updatecart, name="updatecart"),
		path('orderproduct', views.orderproduct, name="orderproduct"),
		#path('productview', views.productview, name="productview")
		path('updateshopingcart/<int:myid>', views.updateshopingcart, name="updateshopingcart"),
		path('updatecolorsize/<int:myid>/<int:cartid>', views.updatecolorsize, name="updatecolorsize"),
		path('ajax_calls/search/', views.autocompleteModel),
		

]