from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.


# says hello to requested name
def hey_you(request: HttpRequest, you) -> HttpResponse:
    return HttpResponse(f"Hey, {you}!")


# tells you your age using a target year and a target birthdate
def age_in(request: HttpRequest, year, birth) -> HttpResponse:
    new_age = year - birth
    return HttpResponse(new_age)


def order_total(request: HttpRequest, burgers, fries, drinks) -> HttpResponse:
    burger_total = burgers * 4.5
    fries_total = fries * 1.5
    drinks_total = drinks * 1
    ultimate_total = burger_total + fries_total + drinks_total
    return HttpResponse(f"{ultimate_total :.1f}")
