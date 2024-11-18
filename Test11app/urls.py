from django.urls import path
from Test11app import views

urlpatterns = [
    path('city-events/', views.display_city_events, name='display_city_events'),
    path('edit-condition/',views.edit_condition, name='edit_condition'),
    path('original-events/',views.original_events_displayed, name='displayed_original_events'),
    path("events/reschedule/", views.reschedule_suggestions, name="reschedule_suggestions"),
]