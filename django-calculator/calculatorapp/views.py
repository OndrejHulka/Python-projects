from django.shortcuts import render
from .forms import NumbersForms
from django.views import View

class Index(View):
    def get(self, request):
        form = NumbersForms()
        return render(request, 'calculator/index.html', {'form': form})

    def post(self, request):
        form = NumbersForms(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            first_selected_option = float(cleaned_data['first_number'])
            second_selected_option = float(cleaned_data['second_number'])

            selected_option = request.POST.get('operation')

            if selected_option == 'addition':
                result = first_selected_option + second_selected_option
                operation = '+'
            
            elif selected_option =='subtraction':
                result = first_selected_option - second_selected_option
                operation = '-'
            
            elif selected_option == 'multiplication':
                result = first_selected_option * second_selected_option
                operation = '*'
            
            else:
                result = first_selected_option/second_selected_option
                operation = '/'
        context = {
            'first_number': first_selected_option,
            'second_number': second_selected_option,
            'operation': operation,
            'result': result
        }
        
        return render(request, 'calculator/result.html', context)
        

        


