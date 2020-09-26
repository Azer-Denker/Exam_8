from django import forms
from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'picture']


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review', 'point']
