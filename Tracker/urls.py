
from django.conf.urls import url
from django.contrib import admin

from TrackerApp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', Home,name='home'),
    url(r'^$', Login, name='login'),
    url(r'^logout/$', Logout, name='logout'),
    url(r'^admin_panel/$', Admin_Panel, name='admin_panel'),
    url(r'^add_vehicle/$', Add_vehicle, name='add_v'),
    url(r'^vehicle_fine/$',Vehicle_fine ,name='vehicle_fine'),
    url(r'^Todays_entry/$', Todays_vehicle,name='today_v'),
    url(r'^entry/$', Entries_by_date, name='entry'),
    url(r'^delete_vehicle/(?P<num>[0-9]+)/$', Delete,name='delete'),
]
