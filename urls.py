from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nanbeige.views.home', name='home'),
    # url(r'^nanbeige/', include('nanbeige.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    ('^version/api/$','nbg.views.version/api')
    ('^version/Android/$','nbg.views.version/Android')
    ('^version/ios/$','nbg.views.version/ios')
    ('^version/notice/$','nbg.views.notice')
)
