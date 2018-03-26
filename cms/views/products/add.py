from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from shop.models import Product, Catalog, ProductClass
from cms.adapters import AdapterProduct
from cms.adapters.exceptions import ProductException


class ProductsAddView(View):
    def get(self, request):
        product = None
        catalogs = Catalog.objects.all()
        pclasess = ProductClass.objects.all()
        return render(request=request, template_name='cms/products/add.html',
                      context={"title_page": "Товары", "product": product, "catalogs": catalogs, "product_class_list": pclasess})

    def post(self, request):
        keys = request.POST.keys()
        prevalidate = {}
        for key in keys:
            if request.POST[key] == '':
                prevalidate[key]='Это обязательное поле'
        if len(prevalidate.keys()) > 0:
            return JsonResponse(data={"errors": prevalidate}, status=400)
        try:
            result = AdapterProduct.create_new_product(form_data=request.POST, files=request.FILES)
        except ProductException as e:
            catalogs = Catalog.objects.all()
            pclasess = ProductClass.objects.all()
            _context = {}
            _context['errors']= e.errors
            return JsonResponse(data=_context, status=400)
        return JsonResponse({'ok': ""})