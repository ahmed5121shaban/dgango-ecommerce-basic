from django.urls import path
from .views import ProductsList,ProcuctDetail,BrandList,BrandDetail,CategoryList,post_list
from .api import product_list_api,product_detail_api,ProductListApi,ProductDetailApi,BrandDetailApi,BrandListApi,CategoryDetailApi,CategoryListApi

app_name = 'products'

urlpatterns = [
    path('test/',post_list),
    path('', ProductsList.as_view(),name='product_list'),
    path('<int:pk>', ProcuctDetail.as_view(),name='product_detail'),
    path('brand/', BrandList.as_view(),name='brand_list'),
    path('brand/<int:pk>', BrandDetail.as_view(),name='brand_detail'),
    path('category/', CategoryList.as_view(),name='category_list'),


    path('api/', product_list_api,name='product_list_api'),
    path('api/<int:id>', product_detail_api,name='product_detail_api'),


    path('api/cbv', ProductListApi.as_view(),name='product_list_cbvapi'),
    path('api/cbv/<int:pk>', ProductDetailApi.as_view(),name='product_detail_cbvapi'),

    path('api/brand/cbv', BrandListApi.as_view(),name='brand_list_cbvapi'),
    path('api/brand/cbv/<int:pk>', BrandDetailApi.as_view(),name='brand_detail_cbvapi'),

    path('api/category/cbv', CategoryListApi.as_view(),name='category_list_cbvapi'),
    path('api/category/cbv/<int:pk>', CategoryDetailApi.as_view(),name='category_detail_cbvapi'),
]