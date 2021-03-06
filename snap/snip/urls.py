import logging
log = logging.getLogger(__name__)

#app specific urls
from django.conf.urls import include, url
from django.contrib import admin
from snip.models import Piece, GlazeLookup, Documentation, Condition, ExhibitionLookup, HeathLineLookup, Logo, MakerLookup, MaterialLookup, MethodLookup, PublicationLookup, SetCollection
from snip.views import MyView
from snip.views import GlazeLookupList
from snip.views import MakerLookupList
from snip.views import PieceDetailView
log.debug('In urls the second')
urlpatterns = [
    url(r'^glaze/$' , GlazeLookupList.as_view(), name = 'glaze-list'),
    url(r'^maker/$' , MakerLookupList.as_view(), name = 'maker-list'),
    url(r'^(?P<slug>[-\w]+)/$' , PieceDetailView.as_view(), name = 'piece-detail'),
    url(r'^mine/$' , MyView.as_view(), name = 'my-view'),
]
