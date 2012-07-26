from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    (r'^$', 'nbg.views.doc_html'),
    (r'^status/$', 'nbg.views.status_html'),

    (r'^app/version/api/$', 'nbg.views_app.version_api'),
    (r'^app/version/android/$', 'nbg.views_app.version_android'),
    (r'^app/version/ios/$', 'nbg.views_app.version_ios'),
    (r'^app/notice/$', 'nbg.views_app.notice'),

    (r'^user/login/email/$', 'nbg.views_user.login_email'),
    # (r'^user/login/weibo/$', 'nbg.views_user.login_weibo'),

    (r'^university/$', 'nbg.views_university.university_list'),
    (r'^university/(\d+)/$', 'nbg.views_university.detail'),

    (r'^course/$', 'nbg.views_course.course_list'),
    (r'^course/assignment/$', 'nbg.views_course.assignment_list'),
    (r'^course/assignment/(\d+)/finish/$', 'nbg.views_course.assignment_finish'),
    (r'^course/assignment/(\d+)/delete/$', 'nbg.views_course.assignment_delete'),
    (r'^course/assignment/(\d+)/modify/$', 'nbg.views_course.assignment_modify'),
    (r'^course/assignment/add/$', 'nbg.views_course.assignment_add'),
    (r'^course/(\d+)/comment/$', 'nbg.views_course.comment_list'),
    (r'^course/(\d+)/comment/add/$', 'nbg.views_course.comment_add'),

    (r'^comment/$', 'nbg.views_comment.comment_list'),

    (r'^study/building/$', 'nbg.views_study.building_list'),
    (r'^study/building/(\d+)/room/$', 'nbg.views_study.room_list'),

    (r'^event/$','nbg.views_event.query'),
    (r'^event/category/$','nbg.views_event.category'),
    (r'^event/(\d+)/$','nbg.views_event.get_event'),
    (r'^event/follow/$','nbg.views_event.follow'),
    (r'^event/following/$','nbg.views_event.following'),

    (r'^wiki/(\d+)/$', 'nbg.views_wiki.wiki_list'),
    (r'^wiki/node/(\d+)/$', 'nbg.views_wiki.wiki_node'),
)
