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
    if request.method == "POST":
        print(request.POST)
        # name
        # symbol
        # utype
        # new_unit = models.Unit.objects.create(unit_name=name,
        #                                       unit_name)

    utypes = models.UnitType.objects.all()
    units  = models.Unit.objects.all()

    type_list = []
    unit_list = []

    for utype in utypes:
        type_list.append({'id': utype.id, 'name': utype.name})

    for unit in units:
        unit_list.append({'id': unit.id, 'name': unit.name, 'symbol': unit.symbol})

    return render(request, "unit/form.html", {
        "type_list": type_list,
        "unit_list": unit_list,
    })

def categoryConfig(request):
    return render(request, "category/category.html")