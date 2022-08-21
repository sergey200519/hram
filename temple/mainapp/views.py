from django.shortcuts import render
from django.views.generic import DetailView, ListView
from mainapp.models import News, ImgNews, Timetable, Settings

# Create your views here.


def index(request):
    context = {
        "title": "Главная"
    }
    return render(request, "mainapp/index.html", context=context)


def schedule(request):
    context = {
        "title": "Расписание",
        "timetable": Timetable.objects.all(),
        "month": Settings.objects.first().month
    }
    return render(request, "mainapp/schedule.html", context=context)


def about_holy(request):
    context = {
        "title": "О святом"
    }
    return render(request, "mainapp/about_holy.html", context=context)


def help(request):
    context = {
        "title": "Помощь храму"
    }
    return render(request, "mainapp/help.html", context=context)


def useful(request):
    context = {
        "title": "Полезное"
    }
    return render(request, "mainapp/useful.html", context=context)


def about_post(request):
    context = {
        "title": "О посте"
    }
    return render(request, "mainapp/about_post.html", context=context)


def christmas_post(request):
    context = {
        "title": "Рождественский пост"
    }
    return render(request, "mainapp/christmas_post.html", context=context)


def post(request):
    context = {
        "title": "Постимся постом приятным"
    }
    return render(request, "mainapp/post.html", context=context)


def about_burial_service(request):
    context = {
        "title": "Отпевания"
    }
    return render(request, "mainapp/about_burial-service.html", context=context)


def about_death(request):
    context = {
        "title": "О смерти, погребении и поминовении усопших"
    }
    return render(request, "mainapp/about_death.html", context=context)


def god(request):
    context = {
        "title": "У Бога все живы"
    }
    return render(request, "mainapp/god.html", context=context)


def commemoration_of_he_dead(request):
    context = {
        "title": "Поминовение усопших"
    }
    return render(request, "mainapp/commemoration_of_he_dead.html", context=context)


def prayers_for_the_dead(request):
    context = {
        "title": "Молитвы о усопших"
    }
    return render(request, "mainapp/prayers_for_the_dead.html", context=context)


def contact(request):
    def my_int(str):
        answer = ""
        for item in str:
            if item.isdigit():
                answer += item
        return answer

    context = {
        "title": "Контакты",
        "settings": Settings.objects.first(),
        "phone_html": my_int(Settings.objects.first().phone)
    }
    return render(request, "mainapp/contact.html", context=context)


class NewsList(ListView):
    model = News
    template_name = "mainapp/news.html"
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["images"] = ImgNews.objects.all()
        context["title"] = "Новсти"
        return context


# def news(request):
#     context = {
#         "title": "Новости",
#         "news": News.objects.all(),
#         "images": ImgNews.objects.all()
#     }
#     return render(request, "mainapp/news.html", context=context)


class NewsDetail(DetailView):
    model = News
    template_name = "mainapp/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["images"] = ImgNews.objects.all()
        context["title"] = "Новсти"
        return context
