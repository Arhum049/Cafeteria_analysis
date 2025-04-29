import re

def extract_table_definitions(sql_file_path, output_file_path):
    """
    Extracts CREATE TABLE statements and their columns from an SQL file.
    
    Args:
        sql_file_path (str): Path to the input SQL file
        output_file_path (str): Path for the output text file
    """
    with open(sql_file_path, 'r', encoding='utf-8') as sql_file:
        sql_content = sql_file.read()

    # Pattern to match CREATE TABLE statements and their columns
    pattern = re.compile(
        r'CREATE TABLE (?:IF NOT EXISTS )?`?(\w+)`?.*?\((.*?)\)[^)]*;',
        re.IGNORECASE | re.DOTALL
    )

    tables = []
    for match in pattern.finditer(sql_content):
        table_name = match.group(1)
        columns_block = match.group(2)
        
        # Clean and split column definitions
        columns = [
            col.strip() 
            for col in columns_block.split('\n') 
            if col.strip() and not col.strip().startswith(('PRIMARY KEY', 'FOREIGN KEY', 'KEY', 'UNIQUE', 'CHECK'))
        ]
        
        tables.append((table_name, columns))

    # Write to output file
    with open(output_file_path, 'w', encoding='utf-8') as out_file:
        for table_name, columns in tables:
            out_file.write(f"TABLE: {table_name}\n")
            for col in columns:
                out_file.write(f"- {col}\n")
            out_file.write("\n")

    print(f"Extracted {len(tables)} tables to {output_file_path}")

# Usage - adjust these paths
sql_file_path = 'your_database_dump.sql'  # Path to your 1GB SQL file
output_file_path = 'table_definitions.txt'
extract_table_definitions(sql_file_path, output_file_path)