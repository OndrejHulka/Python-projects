from django.shortcuts import render, redirect
from .forms import RunForm
from django.views import View
from datetime import time
import math




class Index(View):
    def get(self, request):
        form = RunForm(request.GET)
        return render(request, 'runningcalculator/index.html', {'form': form})


    def post(self,request):
        form = RunForm(request.POST)

        if request.method == 'POST' and form.is_valid():
            
            distance_choice = form.cleaned_data['distance_choice']
            if distance_choice == 60:
                form.cleaned_data['integer_field'] = 0.06
            elif distance_choice == 100:
                form.cleaned_data['integer_field'] = 0.1
            elif distance_choice == 200:
                form.cleaned_data['integer_field'] = 0.2
            elif distance_choice == 400:
                form.cleaned_data['integer_field'] = 0.4
            elif distance_choice == 800:
                form.cleaned_data['integer_field'] = 0.8
            elif distance_choice == 1500:
                form.cleaned_data['integer_field'] = 1.5
            elif distance_choice == 1:
                form.cleaned_data['integer_field'] = 1.6
            elif distance_choice == 5:
                form.cleaned_data['integer_field'] = 5
            elif distance_choice == 10:
                form.cleaned_data['integer_field'] = 10
            elif distance_choice == 21097:
                form.cleaned_data['integer_field'] = 21.097
            elif distance_choice == 42195:
                form.cleaned_data['integer_field'] = 42.195
            elif distance_choice == 50:
                form.cleaned_data['integer_field'] = 50
            elif distance_choice == 100:
                form.cleaned_data['integer_field'] = 100
            elif distance_choice == 100:
                form.cleaned_data['integer_field'] = 160.934
            elif distance_choice == 200:
                form.cleaned_data['integer_field'] = 321.869

            if 'calculate_final_time' in request.POST:
                distance = form.cleaned_data['distance']
                pace_minutes = form.cleaned_data['pace_minutes']
                pace_seconds = (form.cleaned_data['pace_seconds'])/60
                time = time = distance/(60/(pace_minutes + pace_seconds))
                final_hour = math.floor(time)
                final_minutes = (time - final_hour)*60
                final_seconds = abs((final_minutes - math.floor(final_minutes))*60)
                context = {
                    'final_hours': math.floor(final_hour),
                    'final_minutes': math.floor(final_minutes),
                    'final_seconds': math.floor(final_seconds)
                }
                
                return render(request, 'runningcalculator/result_time.html', context)

            
            elif 'calculate_distance' in request.POST:
                hours = (form.cleaned_data['hours'])*60
                minutes = form.cleaned_data['minutes']
                seconds = (form.cleaned_data['seconds'])/60
                pace_minutes = form.cleaned_data['pace_minutes']
                pace_seconds = (form.cleaned_data['pace_seconds'])/60
                equation = (hours + minutes + seconds)/(pace_minutes + pace_seconds)
                unit_choice = form.cleaned_data.get('unit_choice', None)
                if unit_choice == 'Kilometers':
                    unit_choice_s = "km"
                elif unit_choice == 'Miles':
                    unit_choice_s = "mi" 
                else:
                    unit_choice_s = "km"
                
                context = {
                    'final_distance': round(equation, 2),
                    'unit_choice_s': unit_choice_s
                }

                return render(request, 'runningcalculator/result_distance.html', context)

            elif 'calculate_pace' in request.POST:
                hours = (form.cleaned_data['hours'])*60
                minutes = form.cleaned_data['minutes']
                seconds = (form.cleaned_data['seconds'])/60
                distance = form.cleaned_data['distance']
                equation = (hours + minutes + seconds)/distance
                first_number = math.floor(equation)
                second_number = (equation - first_number)*60
                unit_choice = form.cleaned_data.get('unit_choice', None)
                if unit_choice == 'Kilometers':
                    unit_choice_s = "km"
                elif unit_choice == 'Miles':
                    unit_choice_s = "mi" 
                else:
                    unit_choice_s = "km"
                context = {
                    'minutes': math.floor(first_number),
                    'seconds': math.floor(second_number),
                    'unit_choice_s': unit_choice_s
                }

                return render(request, 'runningcalculator/result_pace.html', context)


    




            

            







