import tkinter as tk
import pandas as pd
from tkinter import ttk,messagebox
from predictModule import Predict_price
import matplotlib.pyplot as plt
root= tk.Tk()
root.title("HCMC House Renting Price Prediction")


dummies_data = data_dummies = pd.read_csv('data_dummies.csv')
processed_data = pd.read_csv('processed_data.csv')


# Function to perform prediction when button is clicked
def predict_price_command():
    district = district_var.get()
    acreage = acreage_entry.get()

    if not district or not acreage:
        messagebox.showwarning("Warning", "Please select a district and enter acreage.")
        return
    
    acreage = float(acreage_entry.get())
    predicted_price = Predict_price(district, acreage)
    predicted_price_label.config(text=f"The predicted price is: VND {predicted_price} million", foreground="black")
    # Data visualization - average price by district
    avg_price_by_district = processed_data.loc[processed_data['district']==district].groupby('ward')['price'].mean()
    plt.figure(figsize=(8, 6))
    avg_price_by_district.plot(kind='bar')
    plt.title('Average Price by Ward')
    plt.xlabel('Ward')
    plt.ylabel('Average Price (million VND)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
districts = [col.split('_')[-1] for col in dummies_data.columns if col.startswith('district_')]

# Apply themed styling
style = ttk.Style()
style.theme_use('clam')  # You can try different themes: 'clam', 'alt', 'default', etc.

# StringVar to store selected district
district_var = tk.StringVar(root)

# Frame for padding and styling
main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0)

# Dropdown for district selection
district_label = ttk.Label(main_frame, text="Select District:")
district_label.grid(row=0, column=0, padx=5, pady=5)
district_dropdown = ttk.Combobox(main_frame, textvariable=district_var, values=districts)
district_dropdown.grid(row=0, column=1, padx=5, pady=5)

# Styled number input for acreage
acreage_label = ttk.Label(main_frame, text="Enter Acreage:")
acreage_label.grid(row=2, column=0, padx=5, pady=5)
acreage_entry = ttk.Entry(main_frame, width=10, style='Custom.TEntry')  # Styled Entry widget
acreage_entry.grid(row=2, column=1, padx=5, pady=5)
acreage_unit_label = ttk.Label(main_frame, text="m²")
acreage_unit_label.grid(row=2, column=2, padx=5, pady=5)

# Button to predict
predict_button = ttk.Button(main_frame, text="Predict", command=predict_price_command)
predict_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Label to display predicted price
predicted_price_label = ttk.Label(main_frame, text="")
predicted_price_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
