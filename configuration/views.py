from django.shortcuts import render
from . import models

# Create your views here.
def configMain(request):
    return render(request, "main/settings.html")

def unitConfig(request):
    units = models.Unit.objects.all()

    headers = ["Name", "Symbol", "Ratio", "Type"]

    rows = []

    for unit in units:
        ratio = int(unit.ratio_to_base) if unit.ratio_to_base.is_integer() else unit.ratio_to_base
        ratio_str = f"{ratio} {unit.base_unit.symbol}" if unit.base_unit != None else "Base unit"
        rows.append([unit.unit_name, unit.symbol, ratio_str, unit.unit_type.name])

    print("Rows generated:", rows)

    return render(request, "unit/unit.html", {"headers": headers,
                                              "rows": rows})

def unitCreation(request):
    return render(request, "unit/form.html", {
        "type_list": [{'id': '1', 'name': 'Mass'},
                       {'id': '2', 'name': 'Volume'},
                       {'id': '3', 'name': 'Other'}],
    })

