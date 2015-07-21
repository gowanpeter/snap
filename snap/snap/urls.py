from django.conf.urls import include, url
from django.contrib import admin

import logging
log = logging.getLogger(__name__)

log.debug('In urls the first')
urlpatterns = [
    url(r'^$', 'empty.views.home', name='home'),
    url(r'^snip/', include('snip.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
