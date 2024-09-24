import tkinter as tk
import time
import math

# Create the main window
root = tk.Tk()
root.title("Modern Analog Clock")
root.geometry("500x500")
root.resizable(0, 0)

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Center and radius of the clock
center_x = 250
center_y = 250
clock_radius = 200

# Gradient background function
def create_gradient(canvas, start_color, end_color):
    for i in range(500):
        color = "#%02x%02x%02x" % (int(start_color[0] + (end_color[0] - start_color[0]) * i / 500),
                                   int(start_color[1] + (end_color[1] - start_color[1]) * i / 500),
                                   int(start_color[2] + (end_color[2] - start_color[2]) * i / 500))
        canvas.create_line(0, i, 500, i, fill=color)

# Function to draw the clock face
def draw_clock_face():
    # Draw the gradient background
    create_gradient(canvas, (30, 30, 30), (70, 70, 70))  # Dark to lighter gradient
    
    # Draw the outer circle for the clock face
    canvas.create_oval(center_x - clock_radius, center_y - clock_radius,
                       center_x + clock_radius, center_y + clock_radius, outline="white", width=8)

    # Draw hour markers as minimalistic dots
    for hour in range(12):
        angle = math.radians(hour * 30)
        x_outer = center_x + clock_radius * math.sin(angle)
        y_outer = center_y - clock_radius * math.cos(angle)
        canvas.create_oval(x_outer - 5, y_outer - 5, x_outer + 5, y_outer + 5, fill="white")

# Function to update the clock hands
def update_clock():
    canvas.delete("hands")
    
    # Get the current time
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Draw hour hand (thicker, shorter)
    hour_angle = math.radians((hours + minutes / 60) * 30)
    hour_x = center_x + (clock_radius - 100) * math.sin(hour_angle)
    hour_y = center_y - (clock_radius - 100) * math.cos(hour_angle)
    canvas.create_line(center_x, center_y, hour_x, hour_y, width=10, fill="white", tags="hands", capstyle=tk.ROUND)

    # Draw minute hand (slimmer, longer)
    minute_angle = math.radians((minutes + seconds / 60) * 6)
    minute_x = center_x + (clock_radius - 60) * math.sin(minute_angle)
    minute_y = center_y - (clock_radius - 60) * math.cos(minute_angle)
    canvas.create_line(center_x, center_y, minute_x, minute_y, width=6, fill="light blue", tags="hands", capstyle=tk.ROUND)

    # Draw second hand (slim, modern)
    second_angle = math.radians(seconds * 6)
    second_x = center_x + (clock_radius - 40) * math.sin(second_angle)
    second_y = center_y - (clock_radius - 40) * math.cos(second_angle)
    canvas.create_line(center_x, center_y, second_x, second_y, width=2, fill="red", tags="hands", capstyle=tk.ROUND)

    # Redraw every second
    root.after(1000, update_clock)

# Initial drawing of the clock face
draw_clock_face()

# Start updating the clock hands
update_clock()

# Run the Tkinter event loop
root.mainloop()
