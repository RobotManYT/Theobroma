from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.core.exceptions import ValidationError
from django.contrib import messages
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
        rows.append({"meta": {
                        "id": unit.id,
                        "delete_url": f'delete/{unit.id}/'},
                     "values": {
                        "name": unit.name, 
                        "symbol": unit.symbol, 
                        "ratio": ratio_str, 
                        "type": unit.unit_type.name}})

    print("Rows generated:", rows)

    return render(request, "unit/unit.html", {"headers": headers,
                                              "rows": rows})

def unitCreation(request):
    genForm = True
    oldValue = None
    error_msg = None
    redirect_url = None

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
            messages.success(request, "Item created successfully")
    except (ValueError, ValidationError):
        messages.error(request, "Invalid form")
        error_msg = {"type":"error", "msg":"Invalid form - The unit may already exist or a value may be invalid"}
        oldValue = request.POST
        


    utypes = models.UnitType.objects.all()
    units  = models.Unit.objects.all()

    type_list = []
    unit_list = []

    for utype in utypes:
        type_list.append({'id': utype.id, 'name': utype.name})

    for unit in units:
        unit_list.append({'id': unit.id, 'name': unit.name, 'symbol': unit.symbol})

    if request.method == "POST":
        redirect_url = request.POST.get("redirect_url", "/")
    else:
        redirect_url = request.META.get("HTTP_REFERER", "/")

    return render(request, "unit/form.html", {
        "type_list": type_list,
        "unit_list": unit_list,
        "alert":error_msg,
        "oldValue": oldValue,
        "redirect_url": redirect_url,
    })

def unitModify(request, unit_id):
    unit = get_object_or_404(models.Unit, pk=unit_id)

    if request.method == "POST":
        unit.name = request.POST.get("name")
        unit.symbol = request.POST.get("symbol")
        unit.unit_type_id = request.POST.get("utype")
        unit.base_unit_id = request.POST.get("unit") or None

        try:
            unit.ratio_to_base = float(request.POST.get("ratio"))

            if unit.base_unit_id is None:
                unit.ratio_to_base = 1
            elif unit.ratio_to_base <= 0:
                raise ValueError

            unit.full_clean()
            unit.save()

            messages.success(request, "Unit updated successfully")
            return redirect("unit_config")

        except (ValueError, ValidationError):
            messages.error(request, "Invalid form")

    utypes = models.UnitType.objects.all()
    units = models.Unit.objects.exclude(pk=unit.pk)
    print(f"oldvalue utype: {unit.unit_type_id}, base_unit: {unit.base_unit_id}, ratio: {unit.ratio_to_base}")

    return render(request, "unit/form.html", {
        "type_list": [
            {"id": utype.id, "name": utype.name}
            for utype in utypes
        ],
        "unit_list": [
            {"id": other.id, "name": other.name, "symbol": other.symbol}
            for other in units
        ],
        "oldValue": {
            "name": unit.name,
            "symbol": unit.symbol,
            "utype": unit.unit_type_id,
            "unit": unit.base_unit_id if unit.base_unit else "",
            "ratio": unit.ratio_to_base,
        },
        "editing": True,
        "unit_id": unit.id,
        "redirect_url": request.META.get("HTTP_REFERER", "/"),
    })

@require_POST
def unit_delete(request, unit_id):
    try:
        unit = get_object_or_404(models.Unit, pk=unit_id)
    except models.Unit.DoesNotExist:
        messages.error(request, "Unit not found")
        return HttpResponse(status=404,
                            headers={"HX-Refresh": "true"})

    # Ensure to not break link with child units
    if models.Unit.objects.filter(base_unit=unit).exists():
        messages.error(
            request,
            f"Cannot delete {unit.name}: Used as a reference unit."
        )
        return HttpResponse(status=409,
                            headers={"HX-Refresh": "true"})
    
    unit.delete()
    messages.success(request, "Unit deleted successfully")

    return HttpResponse(
        status=200,
        headers={"HX-Refresh": "true"}
    )

def categoryConfig(request):
    return render(request, "category/category.html")