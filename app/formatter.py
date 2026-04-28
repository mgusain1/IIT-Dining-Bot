
def format_items(rows):
    formatted = []
    for row in rows:
        item_name = row[6]
        protein = row[12]
        calories = row[10]
        parts = [item_name]
        
        if (protein is None or protein == 0) and (calories is None or calories == 0):
            continue
        
        if protein is not None:
            parts.append(f"{protein}g protein")
        
        if calories is not None:
            parts.append(f"{calories} kcal")

        line = " — ".join(parts)
        formatted.append(line)
    return formatted
    