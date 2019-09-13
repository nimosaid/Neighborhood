from django.conf.urls import url
from neighbors import views as neighbors_views
# from projects import views as project_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', neighbors_views.home, name = 'home'),
    url(r'^neighborhoods/$', neighbors_views.all_neighbors, name = 'all_neighbors'),
    # url(r'^neighborhoods/(?P<pk>\d+)/$', neighbors_views.neighborhood_details, name = 'hood-details'),
    url(r'^neighborhoods/(?P<id>\d+)/$', neighbors_views.neighborhood_details, name = 'hood-details'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

