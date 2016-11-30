from django.conf.urls import url, include
from django.contrib import admin
from main.views import IndexView, ChirpDetailView, ProfileUpdateView, ChirpDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^chirp/(?P<pk>\d+)/$', ChirpDetailView.as_view(), name="chirp_detail_view"),
    url(r'^chirp/(?P<pk>\d+)/delete/$', ChirpDeleteView.as_view(), name="chirp_delete_view"),
    url(r'^accounts/profile/$', ProfileUpdateView.as_view(), name="profile_update_view")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
