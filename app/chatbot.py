from db import (
    get_items_by_protein,
    get_items_by_meal,
    get_items_for_date,
    get_top_protein_items_by_meal,
)
from formatter import format_items
from gpt_parser import parse_query_with_gpt


def answer_question(question: str, date_str: str):
    question_lower = question.lower()
    intent = parse_query_with_gpt(question)

    # Fallback to keyword logic if GPT is unavailable
    if intent is None:
        valid_keywords = ["breakfast", "lunch", "dinner", "protein", "menu", "today"]

        if not any(word in question_lower for word in valid_keywords):
            return "Sorry, I didn’t understand that. Try asking about breakfast, lunch, dinner, or protein items."

        meal_slug = None
        wants_protein = "protein" in question_lower

        if "breakfast" in question_lower:
            meal_slug = "breakfast"
        elif "lunch" in question_lower:
            meal_slug = "lunch"
        elif "dinner" in question_lower:
            meal_slug = "dinner"

    else:
        if not intent["valid_query"]:
            return "Sorry, I didn’t understand that. Try asking about breakfast, lunch, dinner, or protein items."

        meal_slug = intent["meal"]
        wants_protein = intent["protein"]

    if wants_protein and meal_slug:
        rows = get_top_protein_items_by_meal(date_str, meal_slug, 5)
        heading = f"Top Protein {meal_slug.capitalize()} Items:"

    elif wants_protein:
        rows = get_items_by_protein(date_str, 5)
        heading = "Top Protein Items:"

    elif meal_slug:
        rows = get_items_by_meal(date_str, meal_slug)
        rows = rows[:10]
        heading = f"{meal_slug.capitalize()} Menu:"

    else:
        rows = get_items_for_date(date_str)
        rows = rows[:15]
        heading = "Today's Menu:"

    if not rows:
        return "No menu items found for that request."

    formatted_rows = format_items(rows)
    return heading + "\n" + "\n".join(formatted_rows)