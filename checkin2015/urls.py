from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Home
    url(r'^$', TemplateView.as_view(template_name='survey/index.html'), name='home'),

    # Checkin page
    url(r'^checkin/$', 'survey.views.add_checkin', name='commuterform'),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^checkin/complete/$', TemplateView.as_view(template_name='survey/thanks.html'), name='complete'),

    # Leaderboard
    url(r'^leaderboard/$', 'leaderboard.views.latest_leaderboard', name="all"),
    url(r'^leaderboard/(?P<size>[\w\.-]*)/$', 'leaderboard.views.latest_leaderboard', name="all"),
    url(r'^leaderboard/subteams/$', 'leaderboard.views.latest_leaderboard_subteams', name="subteams_all"),
    url(r'^leaderboard/subteams/(?P<parentid>[\w\.-]*)/$', 'leaderboard.views.latest_leaderboard_subteams', name="subteams"),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Retail Partners
    url(r'^retail/$', include('retail.urls', namespace='retail'))


) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
