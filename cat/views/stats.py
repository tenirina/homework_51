from django.shortcuts import render

from cat.db import Cat


def stats_view(request):
    select = request.POST.get('select')
    Cat.get_stats(select)
    context = {
        'img_cat': Cat.cat.get('img_cat'),
        'name': Cat.cat.get('name'),
        'age': Cat.cat.get('age'),
        'satiety': Cat.cat.get('satiety'),
        'happiness': Cat.cat.get('happiness'),
        'stat': Cat.cat.get('stat'),
        'last_stat': request.POST.get('select')
    }
    Cat.cat = context
    return render(request, "cat_stats.html", context=context)
