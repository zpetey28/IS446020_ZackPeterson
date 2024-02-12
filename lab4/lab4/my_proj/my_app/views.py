from django.views import View
from django.shortcuts import render, redirect
from . import my_functions, my_objects

def title_name(the_name: str):
    return the_name.title()



class HomePageView(View):
    def get(self, request):
        my_name = "ZACK"

        new_name = title_name(my_name)

        the_names = ['ZACK', 'Mike', 'ETHAN']

        other_names = the_names

        the_names.append('TIM')
        

        new_names = my_functions.title_names(the_names)

        car1 = my_objects.car('green', 'honk honk')

        car2 = my_objects.car('green', 'beep beep')

        the_context = {'hi':'Whats good brother', 
                       'name':new_name, 
                       'names_list': other_names,
                       'car1': car1,
                       'car2': car2
                       }

        return render(request, 'my_app/index.html',the_context)