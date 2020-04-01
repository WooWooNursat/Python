from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Company, Vacancy


@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [company.brief_json() for company in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        return JsonResponse({'data': 'companies post request'})


@csrf_exempt
def one_company(request, id):
    if request.method == 'GET':
        try:
            company = Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            return JsonResponse({'error': 'company does not exist'})
        return JsonResponse(company.to_json())
    elif request.method == 'POST':
        return JsonResponse({'data': 'company post request'})


@csrf_exempt
def comp_vacancies(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'company does not exist'})
    if request.method == 'GET':
        vacancies = Vacancy.objects.filter(company_id=id)
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        return JsonResponse({'data': 'vacancies by company post request'})


@csrf_exempt
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        return JsonResponse({'data': 'vacancies post request'})


@csrf_exempt
def vacancy_detail(request, id):
    if request.method == 'GET':
        try:
            vacancy = Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist:
            return JsonResponse({'error': 'vacancy does not exist'})
        return JsonResponse(vacancy.to_json(), safe=False)
    elif request.method == 'POST':
        return JsonResponse({'data':'vacancy post request'})


@csrf_exempt
def ten_vacancies(request):
    if request.method == 'GET':
        top_ten = Vacancy.objects.all().order_by('-salary')[:10]
        top_ten_json = [vacancy.to_json() for vacancy in top_ten]
        return JsonResponse(top_ten_json, safe=False)
    elif request.method == 'POST':
        return JsonResponse({'error': 'you cannot post here'})