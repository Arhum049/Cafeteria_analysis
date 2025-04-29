
import re
import os

# Input file path (update if needed)
input_file = r"C:\Users\ADMIN\OneDrive\Desktop\ResearchProject\useful_table_definitions.txt"

# Set of 36 useful tables
USEFUL_TABLES = {
    'addons', 'areas', 'branches', 'branch_has_services', 'branch_has_taxes',
    'branch_offer_banners', 'carts', 'categories', 'category_has_dishes',
    'category_has_menus', 'cities', 'companies', 'company_has_regions',
    'company_has_services', 'counters', 'countries', 'country_taxes',
    'currencies', 'discounts', 'dishes', 'dish_extras', 'dish_has_taxes',
    'dish_measurement_units', 'dish_options', 'dish_variants', 'extras',
    'feedback_answers', 'feedback_questions', 'food_licenses', 'footfalls',
    'licenses', 'locations', 'location_discounts', 'location_taxes', 'menus',
    'orders'
}

def extract_table_rows(input_file, useful_tables):
    try:
        # Verify file exists
        if not os.path.exists(input_file):
            print(f"Error: File '{input_file}' not found.")
            return
        
        # Initialize dictionary to store row counts
        table_counts = {table.lower(): 0 for table in useful_tables}
        
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
            # Regex to match "TABLE: table_name (rows: number)"
            pattern = re.compile(r"TABLE:\s*(\w+)\s*\(rows:\s*(\d+)\s*\)")
            
            for line in lines:
                match = pattern.match(line.strip())
                if match:
                    table_name = match.group(1).lower()
                    row_count = int(match.group(2))
                    if table_name in table_counts:
                        table_counts[table_name] = row_count
        
        # Print each table's row count
        print("Row counts for useful tables:")
        for table in sorted(table_counts.keys()):
            print(f"{table}: {table_counts[table]}")
        
        # Calculate and print total count
        total_row_count = sum(table_counts.values())
        print(total_row_count)
        
    except UnicodeDecodeError:
        print(f"Error: File encoding issue. Ensure '{input_file}' is UTF-8 encoded.")
    except Exception as e:
        print(f"Error: {str(e)}")

# Run the script
extract_table_rows(input_file, USEFUL_TABLES)
