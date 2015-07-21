import logging
log = logging.getLogger(__name__)

from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone

from snip.models import Piece, GlazeLookup, Documentation, Condition, ExhibitionLookup, HeathLineLookup, Logo, MakerLookup, MaterialLookup, MethodLookup, PublicationLookup, SetCollection

class MyView(View):

    def get(self, request, *args, **kwargs):
        log.info('In views.MyView')
        boola = models.Piece.after_edith()
        return HttpResponse(boola)


class GlazeLookupList(ListView):
    print("missa luba")
    model = GlazeLookup
   # context_object_name = 'glazes'
    log.debug('in GlazeLookupList')


class MakerLookupList(ListView):
    print("maker luba")
    log.debug('in MakerLookupList')
    model = MakerLookup


class PieceDetailView(DetailView):
    log.debug('in PieceDetailView')
    context_object_name = 'piece'
    queryset = Piece.objects.all()


    #def get_context_data(self, **kwargs):
        #context = super(ArticleDetailView, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        #return context




    #def get(self, request, *args, **kwargs):
        #return HttpResponse('Hello, World!')

    #def get_context_data(self, **kwargs):
        #context = super(ArticleListView, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        #return context




#from django.views.generic.detail import DetailView
#from django.utils import timezone

#from articles.models import Article

#class ArticleDetailView(DetailView):

    #model = Article

    #def get_context_data(self, **kwargs):
        #context = super(ArticleDetailView, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        #return context
#Example myapp/urls.py:

#from django.conf.urls import url

#from article.views import ArticleDetailView

#urlpatterns = [
    #url(r'^(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
#]

#<h1>{{ object.headline }}</h1>
#<p>{{ object.content }}</p>
#<p>Reporter: {{ object.reporter }}</p>
#<p>Published: {{ object.pub_date|date }}</p>
#<p>Date: {{ now|date }}</p>
