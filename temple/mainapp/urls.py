from django.urls import path
from mainapp.views import NewsDetail, NewsList, schedule, about_holy, help, useful, about_post, christmas_post, post, about_burial_service, about_death, god, commemoration_of_he_dead, prayers_for_the_dead, contact

app_name = "mainapp"
urlpatterns = [
    path("", NewsList.as_view(), name="news"),
    path('detail/<int:pk>/', NewsDetail.as_view(), name='detail'),
    path("schedule/", schedule, name="schedule"),
    path("about_holy/", about_holy, name="about_holy"),
    path("help/", help, name="help"),
    path("useful/", useful, name="useful"),
    path("about_post/", about_post, name="about_post"),
    path("christmas_post/", christmas_post, name="christmas_post"),
    path("post/", post, name="post"),
    path("about_burial_service/", about_burial_service, name="about_burial"),
    path("about_death/", about_death, name="about_death"),
    path("god/", god, name="god"),
    path("commemoration_of_he_dead/", commemoration_of_he_dead, name="commemoration_of_he_dead"),
    path("prayers_for_the_dead", prayers_for_the_dead, name="prayers_for_the_dead"),
    path("contact/", contact, name="contact")
]
