from django.conf.urls.defaults import *

from dajaxice.core import dajaxice_autodiscover
from django.conf import settings
from learnajax.example.views import *

dajaxice_autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^learnajax/', include('learnajax.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
	(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
	(r'^$',index),
)
if settings.DEBUG:
    urlpatterns += patterns('',(r'^learnajax/(?P<path>.*)$', 'django.views.static.serve', {'document_root':
	        settings.MEDIA_ROOT}),)
