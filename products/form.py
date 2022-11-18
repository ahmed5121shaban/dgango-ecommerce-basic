from django import forms
from .models import ProductsReview

class ProductsReviewForm(forms.ModelForm):
    class Meta:
        model = ProductsReview
        fields = ['rate','review']
