from django.conf.urls import url
from backendapi import views

urlpatterns = [
    url(r'^api/welcome$', views.welcome),
    url(r'^api/book_list$', views.book_list),
    url(r'^api/author_list$', views.author_list),
    url(r'^api/book/create$', views.create_book),
    url(r'^api/author/create$', views.create_author),
    url(r'^api/view_book/(?P<book_id>\d+)$', views.view_book),
    url(r'^api/view_author/(?P<author_id>\d+)$', views.view_author),
]
