from django import forms


class RunForm(forms.Form):
    UNIT_CHOICES = [
        ('km', 'Kilometers'),
        ('mi', 'Miles'),
    ]

    RACE_CHOICES = [
    (0.06, '60 meters'),
    (0.1, '100 meters'),
    (0.2, '200 meters'),
    (0.4, '400 meters'),
    (0.8, '800 meters'),
    (1.5, '1500 meters'),
    (1.6, '1 mile'),
    (5, '5 kilometers'),
    (10, '10 kilometers'),
    (21.097, 'Half Marathon (21.097 kilometers)'),
    (42.195, 'Marathon (42.195 kilometers)'),
    (50, '50 kilometers'),
    (100, '100 kilometers'),
    (160.934, '100 miles'),
    (321.869, '200 miles'),
]
    
    hours = forms.IntegerField(initial='00', required=False)
    minutes = forms.IntegerField(initial='00', required=False)
    seconds = forms.IntegerField(initial='00', required=False)
    distance = forms.FloatField(required=False)
    unit_choice = forms.ChoiceField(choices=UNIT_CHOICES, required=False)
    distance_choice = forms.ChoiceField(choices=RACE_CHOICES, required=False)
    pace_minutes = forms.IntegerField(initial='00', required=False)
    pace_seconds = forms.IntegerField(initial='00', required=False)