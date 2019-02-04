from django.shortcuts import render,HttpResponse
from .models import Category, Page


def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories':category_list,
                    'pages':pages_list}

    return render(request, 'rango/index.html',context=context_dict)


def about(request):
    return render(request, 'rango/about.html')


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)


def show_page(request, page_id):
    context_dict = {}

    try:
        page = Page.objects.get(pk=page_id)
        context_dict['title'] = page.title
        context_dict['views'] = page.views
        context_dict['category'] = page.category
    except Page.DoesNotExist:
        context_dict['title'] = None
        context_dict['views'] = None
        context_dict['category'] = None

    return render(request, 'rango/page.html',context_dict)
