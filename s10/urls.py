from django.conf.urls import include, url
from django.contrib import admin
from app01 import views

urlpatterns = [
    # Examples:
    # url(r'^$', 's10.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index, name='index'),
    url(r'^host/$',views.host, name='host'),
    url(r'^asset/$',views.asset, name='asset'),
    url(r'^audit/$',views.audit, name='audit'),
    url(r'^accounts/login/$',views.acc_login, name='acc_login'),
    url(r'^logout/$',views.acc_logout, name='acc_logout'),
    url(r'^article/(\d+)/$',views.article, name='article'),
    url(r'^article/create/$',views.create_article, name='create_article'),
]
