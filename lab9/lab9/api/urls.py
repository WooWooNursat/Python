from django.urls import path
from api.views import company_list, one_company, comp_vacancies, vacancy_list, vacancy_detail, ten_vacancies

urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:id>/', one_company),
    path('companies/<int:id>/vacancies/', comp_vacancies),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:id>', vacancy_detail),
    path('vacancies/top_ten', ten_vacancies)
]