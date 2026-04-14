

def normalize_menu(all_menus,date_str):
    normalized_items = []
    for meal_slug, meal_content in all_menus.items():
        meal_name = meal_content["name"]
        menu_data = meal_content["data"]
        category = menu_data["period"]["categories"]
        for category in category:
            category_name = category["name"]
            items = category["items"]
            for itemsin in items:
                item_id = itemsin["id"]
                item_name = itemsin["name"]
                desc = itemsin["desc"]
                portion = itemsin["portion"]
                ingredients = itemsin["ingredients"]
                calories = itemsin["calories"]
                customAllergens = itemsin["customAllergens"]
                nutrients = itemsin["nutrients"]
                proteins = None
                fat = None
                for nutrient in nutrients:
                    if nutrient["name"] == "Protein (g)":
                        proteins = nutrient["valueNumeric"]
                    if nutrient["name"] == "Total Fat (g)":
                        fat = nutrient["valueNumeric"]
                normal = {
                    "date":date_str,
                    "meal_slug":meal_slug,
                    "meal_name":meal_name,
                    "category_name":category_name,
                    "item_id":item_id,
                    "item_name":item_name,
                    "desc":desc,
                    "portion":portion,
                    "ingredients":ingredients,
                    "calories":calories,
                    "Allergens":customAllergens,
                    "Protein_g":proteins,
                    "fat":fat,
                }
                normalized_items.append(normal)
    return normalized_items
                
            
            
        
        