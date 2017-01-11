from django.shortcuts import render, redirect
from openinghours.models import Company, OpeningHours

#TODO: Create function to search and view detailed company
def display_all_companies(request):
    if request.method == "GET":
        companies = Company.objects.all()
        return render(request, 'companies.html', {'companies': companies})

def display_company_by_id(request, id):
    if request.method == "GET":
        import pdb; pdb.set_trace()
        company = Company.objects.get(pk=id)
        opening_hours = OpeningHours.objects.filter(company=company)
        return render(request, 'companies.html', {'companies': companies})
    else:
        pass
