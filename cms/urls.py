from django.urls import path

from cms.views import IndexView
from cms.views import ProductsView
from cms.views import ProductsAddView
from cms.views import ProductsEditView


urlpatterns = [
    path('', IndexView.as_view(), name='cms.index'),
    path('products/', ProductsView.as_view(), name='cms.product.list'),
    path('products/add', ProductsAddView.as_view(), name='cms.product.add'),
    path('products/edit/<int:product_id>', ProductsEditView.as_view(), name='cms.product.edit'),
]
