from django.shortcuts import render
import csv

def inflation_view(request):
    new_list = []
    template_name = 'inflation.html'
    with open("inflation_russia.csv", encoding='utf-8') as f:
        inflation_russia_dict = csv.DictReader(f, delimiter=";")
        for inflation in inflation_russia_dict:
            for month, value in inflation.items():
                if value == '':
                    value = '-'
                    inflation[month] = value
                else:
                    inflation[month] = float(value)
                    print(type(inflation[month]))
                inflation['Год'] = int(inflation['Год'])
            new_list.append(inflation)
    print(new_list)
    # чтение csv-файла и заполнение контекста
    context = {'data': new_list}

    return render(request, template_name, context)
