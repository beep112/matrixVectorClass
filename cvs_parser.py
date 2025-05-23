import os
import csv

def analyze_csv_columns(directory_path):
    column_map = dict()
    all_files = []

    # Read all CSV files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".csv"):
            filepath = os.path.join(directory_path, filename)
            all_files.append(filename)
            try:
                with open(filepath, 'r', newline='', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    headers = next(reader)
                    for col in headers:
                        if col not in column_map:
                            column_map[col] = set()
                        column_map[col].add(filename)
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    return column_map, sorted(all_files)

def export_matrix_to_csv(column_map, all_files, output_path):
    all_columns = sorted(column_map.keys())

    with open(output_path, 'w', newline='', encoding='utf-8') as out_file:
        writer = csv.writer(out_file)

        # Write header
        writer.writerow(["File"] + all_columns)

        # Write each file row
        for file in all_files:
            row = [file]
            for col in all_columns:
                row.append("1" if file in column_map[col] else "0")
            writer.writerow(row)

# Example usage
directory = "/path/to/csv/files"         # Change this to your CSV folder
output_csv = "column_presence_matrix.csv"  # Output CSV file

column_map, files = analyze_csv_columns(directory)
export_matrix_to_csv(column_map, files, output_csv)
print(f"Matrix saved to: {output_csv}")