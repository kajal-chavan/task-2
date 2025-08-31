import pandas as pd

# Sample data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [28, 34, 25, 40, 30],
    "Department": ["HR", "IT", "Finance", "IT", "HR"],
    "Salary": [50000, 60000, 55000, 75000, 52000]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data.csv", index=False)

print("✅ data.csv file created successfully!")

import pandas as pd
from fpdf import FPDF

# Step 1: Read data
data = pd.read_csv("data.csv")

# Step 2: Analyze data
summary = {
    "Total Rows": len(data),
    "Total Columns": len(data.columns),
    "Column Names": ", ".join(data.columns),
    "Missing Values": data.isnull().sum().to_dict()
}

# Step 3: Generate PDF using FPDF
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Automated Data Report", border=False, ln=1, align="C")
        self.ln(5)
    
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def generate_report(data, summary, filename="Report_FPDF.pdf"):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Add Summary
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Data Summary:", ln=True)
    pdf.set_font("Arial", size=12)
    
    for key, value in summary.items():
        pdf.multi_cell(0, 10, f"{key}: {value}")
    
    pdf.ln(5)
    
    # Add Table (First 10 rows)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Data Preview (First 10 rows):", ln=True)
    pdf.set_font("Arial", size=10)
    
    # Column headers
    col_width = pdf.w / (len(data.columns) + 1)
    row_height = 10
    for col in data.columns:
        pdf.cell(col_width, row_height, str(col), border=1, align="C")
    pdf.ln(row_height)
    
    # Rows
    for i, row in data.head(10).iterrows():
        for item in row:
            pdf.cell(col_width, row_height, str(item), border=1, align="C")
        pdf.ln(row_height)
    
    pdf.output(filename)
    print(f"✅ Report generated: {filename}")

# Run function
generate_report(data, summary)
