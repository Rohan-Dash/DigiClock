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

# Function to create a radial gradient background
def create_radial_gradient(canvas, center, radius, color1, color2):
    for i in range(radius):
        ratio = i / radius
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_oval(center_x - i, center_y - i, center_x + i, center_y + i, outline=color, width=2)

# Function to draw the clock face with numbers
def draw_clock_face():
    # Create a modern radial gradient background (from dark to light)
    create_radial_gradient(canvas, (center_x, center_y), clock_radius, (20, 20, 40), (80, 80, 120))  # Dark blue to lighter
    
    # Draw outer circle for the clock
    canvas.create_oval(center_x - clock_radius, center_y - clock_radius,
                       center_x + clock_radius, center_y + clock_radius, outline="white", width=8)

    # Draw hour markers with numbers
    for hour in range(1, 13):
        angle = math.radians(hour * 30)
        x_outer = center_x + (clock_radius - 30) * math.sin(angle)
        y_outer = center_y - (clock_radius - 30) * math.cos(angle)
        
        # Place the hour numbers (1-12)
        x_number = center_x + (clock_radius - 50) * math.sin(angle)
        y_number = center_y - (clock_radius - 50) * math.cos(angle)
        canvas.create_text(x_number, y_number, text=str(hour), font=("Helvetica", 16, "bold"), fill="white")

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
