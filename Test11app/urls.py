from django.urls import path
from Test11app import views

urlpatterns = [
    path('city-events/', views.display_city_events, name='display_city_events'),
    path('edit-condition/',views.edit_condition, name='edit_condition'),
    #path('original-events/',views.original_events_display, name='display_original_events'),
    path('events/', views.display_with_condition, name='display_with_condition'),
    path('special/', views.display_with_special, name='display_with_special'),
    path('reset_modifications/', views.reset_modifications, name='reset_modifications'),
    ]

