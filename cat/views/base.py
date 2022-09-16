from django.shortcuts import render, redirect

from cat.db import Cat


def index_view(request):
    if request.method == "GET":
        return render(request, 'index.html')
    Cat.cat['name'] = request.POST.get('name')
    return redirect("/cat_stats/", request=request)
