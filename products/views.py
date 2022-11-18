from multiprocessing import context, get_context
from django.db.models import Count
from django.views.generic import ListView,DetailView
from .models import Category, Product, ProductsImages, Brand,ProductsReview
from django.shortcuts import render
# Create your views here.
from .form import ProductsReviewForm
from django.views.decorators.cache import cache_page

@cache_page(60)
def post_list(request):
    object = Product.objects.all()
    return render(request,'products/test_list.html',{'products':object})



class ProductsList(ListView):
    model = Product
    paginate_by = 20


class ProcuctDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myproduct = self.get_object()
        context['images'] = ProductsImages.objects.filter(product=myproduct)
        context['related'] = Product.objects.filter(category=myproduct.category)[:10]
        context['reviews'] = ProductsReview.objects.filter(product=myproduct)
        return context

class BrandList(ListView):
    model = Brand


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all().annotate(product_count=Count('product_brand'))
        return context

class BrandDetail(DetailView):
    model = Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        context['brand_product'] = Product.objects.filter(brand=brand)
        return context

class CategoryList(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all().annotate(product_count=Count('product_category'))
        return context

from django.http import JsonResponse
from django.template.loader import render_to_string


def add_reviews(request,id):
    product  = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductsReviewForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.products = product
            myform.user = request.user
            myform.save()

            reviews = ProductsReview.objects.filter(product=product)
            html = render_to_string('include/review.html',{'review':reviews,request:request})
            return JsonResponse({'result':html})



