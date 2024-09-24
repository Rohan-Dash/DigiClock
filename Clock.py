import tkinter as tk
import time
import math

# Create the main window
root = tk.Tk()
root.title("Analog Clock")
root.geometry("400x400")
root.resizable(0, 0)

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Center and radius of the clock
center_x = 200
center_y = 200
clock_radius = 180

# Function to draw the clock face
def draw_clock_face():
    canvas.create_oval(center_x - clock_radius, center_y - clock_radius,
                       center_x + clock_radius, center_y + clock_radius, outline="black", width=4)

    # Draw hour marks
    for hour in range(12):
        angle = math.radians(hour * 30)
        x_outer = center_x + clock_radius * math.sin(angle)
        y_outer = center_y - clock_radius * math.cos(angle)
        x_inner = center_x + (clock_radius - 20) * math.sin(angle)
        y_inner = center_y - (clock_radius - 20) * math.cos(angle)
        canvas.create_line(x_inner, y_inner, x_outer, y_outer, width=3)

# Function to update the clock hands
def update_clock():
    canvas.delete("hands")
    
    # Get the current time
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Draw hour hand
    hour_angle = math.radians((hours + minutes / 60) * 30)
    hour_x = center_x + (clock_radius - 60) * math.sin(hour_angle)
    hour_y = center_y - (clock_radius - 60) * math.cos(hour_angle)
    canvas.create_line(center_x, center_y, hour_x, hour_y, width=6, fill="black", tags="hands")

    # Draw minute hand
    minute_angle = math.radians((minutes + seconds / 60) * 6)
    minute_x = center_x + (clock_radius - 40) * math.sin(minute_angle)
    minute_y = center_y - (clock_radius - 40) * math.cos(minute_angle)
    canvas.create_line(center_x, center_y, minute_x, minute_y, width=4, fill="blue", tags="hands")

    # Draw second hand
    second_angle = math.radians(seconds * 6)
    second_x = center_x + (clock_radius - 20) * math.sin(second_angle)
    second_y = center_y - (clock_radius - 20) * math.cos(second_angle)
    canvas.create_line(center_x, center_y, second_x, second_y, width=2, fill="red", tags="hands")

    root.after(1000, update_clock)

# Draw the clock face once
draw_clock_face()

# Start the clock updates
update_clock()

# Run the Tkinter event loop
root.mainloop()
