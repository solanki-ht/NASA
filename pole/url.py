from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^grid_form/', views.Grid_view),
    url(r'^rover_view/',views.Rover_view),
    url(r'^$',views.menu),
    url(r'^rover_move/',views.rover_move),
    url(r'^sense_form/',views.sensor),
    #url(r'^menu/',views.menu),
    url(r'^update_form/',views.rover_update_form1),
    url(r'^new_mineral/',views.new_mineral1)
       # url(r'^solanki',views.solanki),
)
