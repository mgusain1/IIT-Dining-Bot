import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "menus.db")


def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)


def init_db():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS menu_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        meal_slug TEXT NOT NULL,
        meal_name TEXT NOT NULL,
        category_name TEXT NOT NULL,
        item_id TEXT NOT NULL,
        item_name TEXT NOT NULL,
        description TEXT,
        portion TEXT,
        ingredients TEXT,
        calories INTEGER,
        allergens TEXT,
        protein_g REAL,
        fat REAL
    );
    """

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.commit()


def delete_rows_for_date(date_str: str):
    delete_query = """
    DELETE FROM menu_items
    WHERE date = ?;
    """

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(delete_query, (date_str,))
        conn.commit()


def save_menu_items(normalized_items):
    if not normalized_items:
        return

    date_str = normalized_items[0]["date"]
    delete_rows_for_date(date_str)

    insert_query = """
    INSERT INTO menu_items (
        date,
        meal_slug,
        meal_name,
        category_name,
        item_id,
        item_name,
        description,
        portion,
        ingredients,
        calories,
        allergens,
        protein_g,
        fat
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """

    rows = []

    for item in normalized_items:
        allergens = item.get("Allergens", [])

        if isinstance(allergens, list):
            allergens_str = ", ".join(str(a) for a in allergens)
        else:
            allergens_str = str(allergens) if allergens is not None else ""

        calories = item.get("calories")
        try:
            calories = int(calories) if calories is not None else None
        except (TypeError, ValueError):
            calories = None

        protein_g = item.get("Protein_g")
        try:
            protein_g = float(protein_g) if protein_g is not None else None
        except (TypeError, ValueError):
            protein_g = None

        fat = item.get("fat")
        try:
            fat = float(fat) if fat is not None else None
        except (TypeError, ValueError):
            fat = None

        rows.append(
            (
                item.get("date"),
                item.get("meal_slug"),
                item.get("meal_name"),
                item.get("category_name"),
                item.get("item_id"),
                item.get("item_name"),
                item.get("desc"),
                item.get("portion"),
                item.get("ingredients"),
                calories,
                allergens_str,
                protein_g,
                fat,
            )
        )

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.executemany(insert_query, rows)
        conn.commit()


def get_items_for_date(date_str: str):
    query = """
    SELECT *
    FROM menu_items
    WHERE date = ?
    ORDER BY meal_slug, category_name, item_name;
    """

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (date_str,))
        rows = cursor.fetchall()

    return rows


def get_items_by_meal(date_str: str, meal_slug: str):
    query = """
    SELECT *
    FROM menu_items
    WHERE date = ? AND meal_slug = ?
    ORDER BY category_name, item_name;
    """

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (date_str, meal_slug))
        rows = cursor.fetchall()

    return rows


def get_items_by_protein(date_str: str, limit: int = 10):
    query = """
    SELECT *
    FROM menu_items
    WHERE date = ? AND protein_g IS NOT NULL
    ORDER BY protein_g DESC
    LIMIT ?;
    """

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (date_str, limit))
        rows = cursor.fetchall()

    return rows


def get_top_protein_items_by_meal(date_str: str, meal_slug: str, limit: int = 10):
    query = """
    SELECT *
    FROM menu_items
    WHERE date = ? AND meal_slug = ? AND protein_g IS NOT NULL
    ORDER BY protein_g DESC
    LIMIT ?;
    """

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (date_str, meal_slug, limit))
        rows = cursor.fetchall()

    return rows