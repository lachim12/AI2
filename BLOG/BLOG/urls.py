from django.conf.urls import *

from django.contrib import *

from django.http import *

from django.views.generic import *



admin.autodiscover()


urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),

	url(r'^/?$', 'news.views.news_list', name='news-list'),
   	url(r'^(?P<page>[0-9]+)/$', 'news.views.news_list', name='news-list'),
	url(r'^/?$', 'news.views.news_list', name='news-list'),
	#do widoku jednej wiadomosci
	url(r'^news/(?P<slug>[\w\-_]+)/$', 'news.views.news_detail', name='news-detail'),
	#do widoku po kategoriach
	url(r'^category/(?P<slug>[\w\-_]+)/(?P<page>[0-9]+)/$', 'news.views.category_news_list', name='category-news-list'),
	url(r'^category/(?P<slug>[\w\-_]+)/$', 'news.views.category_news_list', name='category-news-list'),
	#podstrony
	
	url(r'^kontakt/$', TemplateView.as_view(template_name="kontakt.html")),
	url(r'^kate/$', TemplateView.as_view(template_name="kategorie.html")),

)

