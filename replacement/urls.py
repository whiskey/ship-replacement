## replacement urls
from django.conf.urls.defaults import *
import settings

urlpatterns = patterns('django.views.static',
    (r'^media/(?P<path>.*)$', 
        'serve', {
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': True }),)

urlpatterns += patterns('eve.replacement.views',
    # Index page
    (r'^$', 'index'),
    (r'^markTicket/(?P<ticketID>\d)$', 'markTicket'),
    (r'^deleteTicket/(?P<ticketID>\d)$', 'deleteTicket'),
    
    # user handling
    (r'^register$', 'registerUser'),
    (r'^login$', 'loginUser'),
    (r'^logout$', 'logoutUser'),
)