from django.urls import path

from webapp.views.__init__ import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/add-review/', ReviewForProductCreateView.as_view(), name='product_review_create'),
    path('review/<int:pk>/edit/', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
]

app_name = 'webapp'
