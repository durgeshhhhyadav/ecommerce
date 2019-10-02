from django import forms
from module1.models import LoginData,AddProduct,SubProduct


class LoginForm(forms.Form):
	username = forms.EmailField(label='username',widget=forms.TextInput(attrs={'class':'special','size':'45','autocomplete': "off"}))
	password  = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'special','size':'45'}))

class SignupForm(forms.Form):
	firstname = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'firstname'}))
	lastname = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'lastname'}))
	email    = forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder': 'Email','class':'special','size':'45'}))
	mobileno = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'mobileno','class':'special','size':'45'}))
	password = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'password'}))
	repassword = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 're-password'}))

	CHOICES=[('male','male'),('female','female')]
	gender =forms.ChoiceField(label='', choices=CHOICES, widget=forms.RadioSelect)


class AddProductForm(forms.Form):
	name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'name','class':'special','size':'45'}))
	image1 = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'image1','class':'special','size':'45'}))
	image2 = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'image2','class':'special','size':'45'}))
	image3 = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'image3','class':'special','size':'45'}))
	category = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'category','class':'special','size':'45'}))
	price = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'price'}))
	

	
class SubProductForm(forms.Form):
	color = forms.CharField(required=False, label='',widget=forms.TextInput(attrs={'placeholder': 'color'}))
	size = forms.CharField(required=False, label='',widget=forms.TextInput(attrs={'placeholder': 'size'}))
	price = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'price'}))
	
	quantity = forms.CharField(required=False,label='',widget=forms.TextInput(attrs={'placeholder': 'quantity','class':'special','size':'45'}))
	
	discount = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'discount'}))

	
