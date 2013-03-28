from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'AppClient.views.home', name='home'),
    url(r'^create_user', 'AppClient.views.create_user', name=''),
    url(r'^todo', 'AppClient.views.todo', name=''),
    url(r'^create_todo', 'AppClient.views.createtodo', name=''),


    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'AppClient/templates/'}),
    # url(r'^NikeAppClient/', include('NikeAppClient.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
