import re

# List of the 36 useful tables
useful_tables = {
    "orders", "dishes", "carts", "branches", "categories", "footfalls", 
    "feedback_answers", "feedback_questions", "menus", "dish_variants", 
    "addons", "extras", "dish_extras", "category_has_dishes", "category_has_menus", 
    "dish_has_taxes", "dish_measurement_units", "dish_options", "branch_has_taxes", 
    "branch_offer_banners", "companies", "counters", "areas", "locations", 
    "location_taxes", "location_discounts", "branch_has_services", 
    "company_has_services", "company_has_regions", "discounts", "country_taxes", 
    "currencies", "cities", "countries", "food_licenses", "licenses"
}

# Input and output file paths
input_file = "table_definitions.txt"
output_file = "useful_table_definitions.txt"

def extract_useful_tables(input_file, output_file, useful_tables):
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        # Variables to store extracted schema
        extracted_schema = []
        current_table = None
        table_block = []
        
        # Parse the file line by line
        for line in lines:
            line = line.strip()
            
            # Match table name (e.g., "TABLE: orders")
            table_match = re.match(r"TABLE: (\w+)", line)
            if table_match:
                # If we were collecting a table block, process the previous one
                if current_table:
                    if current_table.lower() in useful_tables:
                        extracted_schema.extend(table_block)
                        extracted_schema.append("")  # Add blank line for readability
                
                # Start a new table block
                current_table = table_match.group(1)
                table_block = [line]
            elif line and current_table:
                # Add column or comment lines to the current table block
                table_block.append(line)
        
        # Process the last table block
        if current_table and current_table.lower() in useful_tables:
            extracted_schema.extend(table_block)
        
        # Write the extracted schema to the output file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(extracted_schema))
        
        print(f"Successfully extracted {len(set(table.lower() for table in useful_tables))} useful tables to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")

# Run the extraction
extract_useful_tables(input_file, output_file, useful_tables)