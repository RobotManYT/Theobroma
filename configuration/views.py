from django.shortcuts import render
from . import models
from django.core.exceptions import ValidationError

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
        rows.append([unit.name, unit.symbol, ratio_str, unit.unit_type.name])

    print("Rows generated:", rows)

    return render(request, "unit/unit.html", {"headers": headers,
                                              "rows": rows})

def unitCreation(request):
    genForm = True
    oldValue = None

    try:
        if request.method == "POST":
            genForm = False
            # print(request.POST)

            unit_creation = models.Unit()
            
            unit_creation.name = request.POST.get("name")
            unit_creation.symbol = request.POST.get("symbol")
            unit_creation.unit_type_id = request.POST.get("utype")
            unit_creation.base_unit_id = request.POST.get("unit") if request.POST.get("unit") != "" else None
            unit_creation.ratio_to_base = float(request.POST.get("ratio"))

            # Custom validation
            if unit_creation.base_unit == None or unit_creation.base_unit == "":
                unit_creation.base_unit = None
                unit_creation.ratio_to_base = 1
            else:
                if unit_creation.ratio_to_base <= 0:
                    print(f"Invalid form - ratio_to_base of 0 or under is a bit confusing, please retry")
                    raise ValueError

            # Django full validation
            try:
                unit_creation.full_clean()
            except ValueError:
                # Failure - Invalid form
                print("Invalid form - Please retry")
                raise ValueError

            print(f"Saving...")
            print(unit_creation)

            unit_creation.save()
    except ValueError:
        oldValue = request.POST
        


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
        "oldValue": oldValue,
        "redirect_url": request.META.get("HTTP_REFERER"),
    })

def categoryConfig(request):
    return render(request, "category/category.html")