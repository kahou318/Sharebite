from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from restaurant.models import MenuSection
import json


# Deals with the operations involving changes to overall Menu Section table.
# Operations: 'GET' Get all menu sections
#             'POST' Adds new menu section to database
def menu_sections(request):
    if request.method == 'GET':
        try:
            all_menu_sections = get_all_sections()
            return JsonResponse({"MenuSection": all_menu_sections})
        except:
            return HttpResponse("Error has occurred retrieving Menu Sections.")
    elif request.method == 'POST':
        try:
            added_section = add_section(request)
            return JsonResponse({"success": True,
                                 "MenuSection": added_section})
        except:
            return HttpResponse("Error has occurred adding new Menu Section to the database.")
    else:
        return HttpResponse("Request method not recognized. Only GET and POST are supported.")


# Deals with operations involving specific entry in Menu Section table.
# Operations: 'GET' Retrieves an entry from table
#             'POST' Edits an entry in table
#             'DELETE' Delete an entry from table
def specific_menu_section(request, section_id):
    if request.method == 'GET':
        try:
            menu_section = get_section(request, section_id)
            return JsonResponse({"MenuSection": menu_section})
        except:
            return HttpResponse("Error has occurred retrieving from database")
    elif request.method == 'POST':
        # return HttpResponse(list(edit_section(request, section_id)))
        # try:
        return JsonResponse({"success": True,
                             "MenuSection": edit_section(request, section_id)})
        # except:
        #     return HttpResponse("Error has occurred editing entry in database.")
    elif request.method == 'DELETE':
        try:
            delete_section(section_id)
            return JsonResponse({"success": True})
        except:
            return HttpResponse("Failed to delete from database.")
    else:
        return HttpResponse("Request method not recognized. Only DELETE, GET and POST are supported.")


# Function to retrieve all Menu Sections from the database
# Returns the entries in a list
def get_all_sections():
    list_of_sections = list(MenuSection.objects.all().values())
    return list_of_sections


# Retrieves the menu section with specified ID from database.
# Returns the menu section object as a list, or None if not found
def get_section(request, section_id):
    menu_section = MenuSection.objects.filter(id=section_id).values().first()
    if menu_section is None:
        return None
    else:
        return [menu_section]


# Adds a new section to the database
# Returns the added section as a list
def add_section(request):
    section_name = get_request_data(request, 'name')
    new_section = MenuSection(name=section_name)
    new_section.save()
    return [model_to_dict(new_section)]


# Edits the menu section entry in the database with new data from the request
# Returns the edited menu entry in a list
def edit_section(request, section_id):
    # Retrieve the new name of menu section
    new_name = get_request_data(request, 'name')
    # Retrieve object to be edited
    db_query = MenuSection.objects.filter(id=section_id)
    menu_section = db_query
    db_query.update(name=new_name)
    return list(menu_section.values())


# Takes an id of a section as input
# Deletes the entry in the menu section table with corresponding id
# Returns the number of objects deleted
def delete_section(section_id):
    menu_section = MenuSection.objects.filter(id=section_id).first()
    return menu_section.delete()


# Takes as input the request and a key of the request body
# Decodes the request body and returns the value associated with the input key
# Returns the value associated with the key
def get_request_data(request, key):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    return body[key]
