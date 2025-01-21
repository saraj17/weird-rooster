import csv
from collections import defaultdict

# Define your keywords for grouping
keywords = ['ssc', 'tech', 'edu', 'gov', 'com']

# Function to assign domain to group based on keywords
def get_group(domain):
    for keyword in keywords:
        if keyword.lower() in domain.lower():  # Case-insensitive matching
            return keyword
    return 'other'  # Default group for domains that don't match any keyword

# Read the CSV file
input_file = 'your_file.csv'  # Replace with your actual CSV file name
grouped_domains = defaultdict(list)

with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        domain = row['Domain']
        group = get_group(domain)
        grouped_domains[group].append(domain)

# Output grouped domains in a table format
# Create a CSV output with groups as columns
output_file = 'grouped_domains.csv'  # Output CSV file for grouped domains

# Write the grouped domains to a new CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    
    # Write header
    writer.writerow(['Group', 'Domains'])
    
    # Write each group and its domains
    for group, domains in grouped_domains.items():
        writer.writerow([group, ', '.join(domains)])

print(f"Grouped domains have been saved to {output_file}")
