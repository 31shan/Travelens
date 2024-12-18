from django.db import models
import random

# Create your models here.


class CheckTab(models.Model):
    slot_choices = [
        ('FN', 'Forenoon'),
        ('AN', 'Afternoon'),
        ('EVE', 'Evening'),
    ]

    id = models.IntegerField(blank=True, primary_key=True)
    city = models.TextField(max_length=50, blank=True, null=True)
    date = models.IntegerField(blank=True, null=True)
    slot_of_day = models.TextField(max_length=3, choices=slot_choices, blank=True, null=True)
    event = models.TextField(max_length=50, blank=True, null=True)
    special = models.TextField(max_length=50, blank=True, null=True)
    temperature = models.IntegerField(blank=True, null=True)
    condition = models.TextField(max_length=50, blank=True, null=True)

    original_condition = models.TextField(max_length=50, blank=True, null=True)
    is_modified = models.BooleanField(default=False)

    #is_missed = models.BooleanField(default=False)
    priority = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return f"{self.city} - {self.event} ({self.slot_of_day} - Date {self.date}) temperature: {self.temperature} Current Weather: {self.condition}"



    def save(self, *args, **kwargs):
        if self.special:
            if self.condition != self.original_condition:
                self.is_modified = True
            else:
                self.is_modified = False

        super().save(*args, **kwargs)


    def generate_priority(self):
        self.priority = random.choice([1, 2, 3])
        self.save()

    def revert_condition(self):
        self.condition = self.original_condition
        self.is_modified = False
        self.priority = None
        self.save()

    def get_display_condition(self, prioritize_special=False):
        if prioritize_special and self.special:
            return self.special
        return self.condition

