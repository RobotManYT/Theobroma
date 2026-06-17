''' WORK IN PROGRESS '''

from django.shortcuts import render, redirect
from django.contrib import messages

# from . import models

# Create your views here.
def inventory(request):
    return render(request, "inventory/inventory.html", { 
        "inventory_items": [
            {
                "name": "Poudre de cacao",
                "category": "Ingrédient sec",
                "stock": 42,
                "unit": "kg",
                "stock_value": 210.0,
                "unit_price": 5.0,
            },
            {
                "name": "Sucre glace",
                "category": "Édulcorant",
                "stock": 18,
                "unit": "kg",
                "stock_value": 54.0,
                "unit_price": 3.0,
            },
            {
                "name": "Beurre de cacao",
                "category": "Matière grasse",
                "stock": 0,
                "unit": "kg",
                "stock_value": 0.0,
                "unit_price": 8.0,
            },
        ]
    })

def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")

        print(name)
        print(quantity)

        # return redirect("inventory:list")
        # return render(request, "inventory/create.html")

        # return redirect("inventory:create")


    messages.error(request, "Item created successfully") # Display a temporary banner
    return render(request, "inventory/create.html", {
        "category_list": [{'id': 1, 'name': 'Cocoa'}, 
                          {'id': 2, 'name': 'Dairy Products'}, 
                          {'id': 3, 'name': 'Sugar'}, 
                          {'id': 4, 'name': 'Nuts & Dry fruits'}, 
                          {'id': 5, 'name': 'Others'}],
        "utype_list": [{'id': '1', 'name': 'Mass'},
                       {'id': '2', 'name': 'Volume'},
                       {'id': '3', 'name': 'Other'}],
        "unit_list": [{'id': '1', 'name': 'Kilogram', 'symbol': 'kg', 'type': '1'},
                      {'id': '2', 'name': 'Gram', 'symbol': 'g', 'type': '1'},
                      {'id': '3', 'name': 'Litre', 'symbol': 'L', 'type': '2'},
                      {'id': '4', 'name': 'Millilitre', 'symbol': 'mL', 'type': '2'},
                      {'id': '5', 'name': 'Piece(s)', 'symbol': 'pcs', 'type': '3'}],

        "oldValue": request.POST,

        "error": "lol", # Display a message at the top of the page with the message
    })