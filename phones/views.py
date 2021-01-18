from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort_arg = request.GET.get('sort')
    all_phones = Phone.objects.all()
    if sort_arg == 'name':
        all_phones = all_phones.order_by('name')
    if sort_arg == 'min_price':
        all_phones = all_phones.order_by('price')
    if sort_arg == 'max_price':
        all_phones = all_phones.order_by('-price')
    context = {'phones': all_phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).first()
    context = {'phone': phone}
    return render(request, template, context)
