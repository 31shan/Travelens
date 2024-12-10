from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import CheckTab
from django.db.models import F
import random

# Create your views here.



def display_city_events(request):
    city_name = request.GET.get('city')
    events = CheckTab.objects.filter(city=city_name) if city_name else CheckTab.objects.none()


    return render(request, 'display_city_events.html', {
        'city': city_name,
        'events': events,
    })


def edit_condition(request):
    if request.method == 'POST':
        record_id = request.POST.get('record_id')
        new_condition = request.POST.get('condition')


        record = get_object_or_404(CheckTab, id=record_id)
        record.condition = new_condition
        record.save()  # This triggers the save method to mark it as modified
        return redirect('display_city_events')  # Redirect back to city events view

    # If GET, just render the form to search by ID
    return render(request, 'edit_condition.html')


'''
def original_events_display(request):

    city = request.GET.get('city', '')
    prioritize_special = request.GET.get('prioritize_special', 'false').lower() == 'true'

    # Filter events based on the city
    events = None
    if city:
        events = CheckTab.objects.filter(city__icontains=city)
        # Set display_condition based on prioritize_special
        for event in events:
            event.display_condition = event.get_display_condition(prioritize_special=prioritize_special)

    return render(request, 'display_events.html', {
        'events': events,
        'city': city,
        'prioritize_special': prioritize_special,
    })
'''

#######

'''
def updated_events_display(request):
    city = request.GET.get("city")
    prioritize_special = request.GET.get("prioritize_special") == "true"

    events = CheckTab.objects.filter(is_missed=False)
    if city:
        events = events.filter(city=city)

    if prioritize_special:
        for event in events:
            if event.special:
                event.condition = event.special  # Temporarily apply special conditions

    return render(request, "events.html", {
        "events": events.order_by("date", "slot_of_day"),
        "city": city,
        "prioritize_special": prioritize_special
    })


def reschedule_suggestions(request):
    missed_event_id = request.GET.get("missed_event_id")
    missed_event = CheckTab.objects.get(id=missed_event_id)

    if missed_event.date == 5:  # Last day; cannot reschedule
        return render(request, "no_reschedule.html", {"event": missed_event})

    # Suggest replacement based on priority from next day's events
    next_day_events = CheckTab.objects.filter(date=missed_event.date + 1, is_missed=False).order_by("-priority")
    suggested_replacement = next_day_events.first() if next_day_events else None

    if request.method == "POST" and "confirm" in request.POST:
        if suggested_replacement:
            suggested_replacement.is_missed = True  # Temporarily mark replacement as missed
            missed_event.date += 1  # Reschedule missed event
            missed_event.save()
            suggested_replacement.save()
        return redirect("original_events_displayed")

    return render(request, "reschedule_suggestions.html", {
        "missed_event": missed_event,
        "suggested_replacement": suggested_replacement,
    })
'''
######

def display_with_condition(request):
    city = request.GET.get('city', '')
    events = CheckTab.objects.filter(city__iexact=city)
    for event in events:
        event.condition = event.original_condition

        event.save()
    return render(request, 'events.html', {'events': events, 'show_special': False, 'city': city,})

def display_with_special(request):
    city = request.GET.get('city', '')
    events = CheckTab.objects.filter(city__iexact=city)
    for event in events:
        if event.special:
            event.condition = event.special
            if event.condition != event.original_condition:
                event.is_modified = True
        event.save()
    return render(request, 'events.html', {'events': events, 'show_special': True, 'city': city,})

def reset_modifications(request):
    city = request.GET.get('city', '')
    events = CheckTab.objects.filter(city__iexact=city)
    for event in events:
        event.revert_condition()
        event.generate_priority()
    return render(request, 'events.html', {'events': events, 'show_special': False, 'city': city,})




