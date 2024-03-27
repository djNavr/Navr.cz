from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from ..forms import *

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        #print("REquest type ", type(request))
        if form.is_valid():
            # Spracujte dáta z form.cleaned_data
            field1_data = form.cleaned_data['field1']
            field2_data = form.cleaned_data['field2']
            # Vykonajte akcie s načítanými dátami

            print(f"f1 {field1_data}")
            print(f"f2 {field2_data}")
        return redirect("members")

    form = MyForm()

    return render(request, 'basicform.html', {'form': form})

def member_form(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("members")

    else:
        form = MemberForm()

    return render(request, "member_form.html", {"form": form})