from django import forms
from .models import Products
# from models import Products


class ProductForm(forms.ModelForm):
               class Meta:
                              model = Products
                              fields = '__all__'
                              labels = {
                                        'product_id':'Product ID',
                                        'product_name':'Product Name',
                              'sku':'SKU',
                              'price':'Price',
                              'quantity':'Quantity','supplier':'Supplier'
                              }
               Widgets={
                              'product_id':forms.NumberInput(attrs={'placeholder':'e.g 1','class':'form-control'}),
                              'product_name':forms.TextInput(attrs={'placeholder':'bread','class':'form-control'}),
                              'sku':forms.NumberInput(attrs={'placeholder':'SR6778','class':'form-control'}),
                              'price':forms.NumberInput(attrs={'placeholder':'1000','class':'form-control'}),
                              'quantity':forms.NumberInput(attrs={'placeholder':'10','class':'form-control'}),
                              'supplier':forms.TextInput(attrs={'placeholder':'WASUPPLY','class':'form-control'}),
                      }         
               