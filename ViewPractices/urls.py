from django.conf.urls import patterns, url

from myformapp.views import homePage,NewContact, MyView, ContactRedirectView
from django.views.generic.base import RedirectView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ViewPractices.views.home', name='home'),
    # url(r'^ViewPractices/', include('ViewPractices.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', homePage.as_view()),
    url(r'^createcontact/$', NewContact.as_view()),
    
    url(r'^myview/$', MyView.as_view(), name='my-view'),
    url(r'^(?P<pk>\d+)/$', ContactRedirectView.as_view(), name='contact-counter'),
    url(r'^go-to-django/$', RedirectView.as_view(url='http://djangoproject.com'), name='go-to-django'),
)
