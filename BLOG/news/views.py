from django.template import *
from django.shortcuts import *

from news.models import *

from django.views import generic
from news import models


from django.views.generic import TemplateView
from django.http import HttpResponse




def index(request):
    news = News.objects.all().order_by('-posted_date')			#zmienna news - sortowanie po dacie
    return render_to_response('news_list.html',
            {'news': news},
            context_instance=RequestContext(request))


class NewsList(generic.ListView):
    model = models.News
    paginate_by = 10                        #ilosc wiadomosci na 1 stronie
    context_object_name = 'news_list'       #nazwa zmiennej, pod ktora lista wiadomosci bedzie dostepna w szablonie.

news_list = NewsList.as_view()


#widok jednej wiadomosci
class NewsDetailView(generic.DetailView):
    model = models.News

news_detail = NewsDetailView.as_view()


#widok po kategoriach
#NewsList dziedziczy ListView
class CategoryNewsList(NewsList): 					
    template_name = 'news/category_news_list.html'

    #pozwala przekazac dane do szablonu
    #perator super pozwala nam pobrac istniejacy kontekst i dodac do niego rekord kategorii.
    def get_context_data(self, **kwargs):
        context = super(CategoryNewsList, self).get_context_data(**kwargs)
        context['category'] = self._get_category()
        return context

    #okreslamy jakie wiadomosci maja byc wyswietlane - te przypisane do wybranej kategorii
    def get_queryset(self):
        category = self._get_category()
        return models.News.objects.filter(categories=category)

    def _get_category(self):
        return models.Category.objects.get(slug=self.kwargs['slug'])

category_news_list = CategoryNewsList.as_view()


