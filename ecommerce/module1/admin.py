from django.contrib import admin
from module1.models import LoginData,AddProduct,AddToCart,SubProduct
# Register your models here.
admin.site.register(LoginData)
admin.site.register(AddProduct)
admin.site.register(AddToCart)
admin.site.register(SubProduct)