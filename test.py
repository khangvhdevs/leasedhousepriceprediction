import tkinter as tk
import random

# Step 1: Prepare the Data
data = []
timestamp = 0
for _ in range(100):
   data.append((timestamp, random.randint(0, 100)))
   timestamp += 1

# Step 2: Design the GUI
window = tk.Tk()
window.geometry("720x500")
window.title("Time-Series Data Visualization")

label = tk.Label(window, text="Time-Series Data Visualization")
label.pack()

canvas_width = 800
canvas_height = 400
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Step 3: Plotting the Time-Series Data
def plot_data():
   x_scale = canvas_width / len(data)
   y_scale = canvas_height / 100

   for i in range(len(data) - 1):
      x1 = i * x_scale
      y1 = canvas_height - data[i][1] * y_scale
      x2 = (i + 1) * x_scale
      y2 = canvas_height - data[i + 1][1] * y_scale

      canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)

plot_data()

# Step 4: Adding Interactivity
def update_data():
   # Generate new random data
   data.clear()
   timestamp = 0
   for _ in range(100):
      data.append((timestamp, random.randint(0, 100)))
      timestamp += 1

   # Clear the canvas and replot the data
   canvas.delete("all")
   plot_data()

button = tk.Button(window, text="Update Data", command=update_data)
button.pack()

# Step 5: Enhancing the Visualization
x_label = tk.Label(window, text="Time")
x_label.pack()

y_label = tk.Label(window, text="Value")
y_label.pack()

# Step 6: Finalize and Refine
# Additional refinements can be made here based on specific requirements

# Start the Tkinter event loop
window.mainloop()