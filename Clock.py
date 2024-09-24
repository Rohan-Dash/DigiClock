import tkinter as tk
from tkinter import colorchooser
import time
import math

# Create the main window (windowless, borderless)
root = tk.Tk()
root.geometry("500x500")
root.overrideredirect(True)  # Removes the window border and title bar
root.wm_attributes("-transparentcolor", "black")  # Makes black background transparent

canvas = tk.Canvas(root, width=500, height=500, bg="black", highlightthickness=0)
canvas.pack()

# Center and radius of the clock
center_x = 250
center_y = 250
clock_radius = 200

# Variables to track the position of the window for dragging
start_x = 0
start_y = 0

# Default clock colors
clock_color = "white"
hand_color = "light blue"
second_hand_color = "red"

# Function to allow the window to be dragged
def start_move(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y

def do_move(event):
    x = root.winfo_x() + (event.x - start_x)
    y = root.winfo_y() + (event.y - start_y)
    root.geometry(f"+{x}+{y}")

# Bind the functions to mouse events for dragging
canvas.bind("<Button-1>", start_move)
canvas.bind("<B1-Motion>", do_move)

# Function to draw the clock face without the outer circle
def draw_clock_face():
    canvas.delete("face")

    # Draw hour markers with numbers only (no outer circle)
    for hour in range(1, 13):
        angle = math.radians(hour * 30)
        x_number = center_x + (clock_radius - 50) * math.sin(angle)
        y_number = center_y - (clock_radius - 50) * math.cos(angle)
        canvas.create_text(x_number, y_number, text=str(hour), font=("Helvetica", int(clock_radius * 0.1), "bold"), fill=clock_color, tags="face")

    # Create the settings button below the 6-hour mark
    button_x = center_x
    button_y = center_y + (clock_radius - 20)
    canvas.create_oval(button_x - 10, button_y - 10, button_x + 10, button_y + 10, fill="gray", tags="face")
    canvas.create_text(button_x, button_y, text="⚙", font=("Helvetica", 10), fill="white", tags="face")
    
    # Bind click to open settings window
    canvas.tag_bind("face", "<Button-1>", open_settings)

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
    canvas.create_line(center_x, center_y, hour_x, hour_y, width=int(clock_radius * 0.05), fill=hand_color, tags="hands", capstyle=tk.ROUND)

    # Draw minute hand (slimmer, longer)
    minute_angle = math.radians((minutes + seconds / 60) * 6)
    minute_x = center_x + (clock_radius - 60) * math.sin(minute_angle)
    minute_y = center_y - (clock_radius - 60) * math.cos(minute_angle)
    canvas.create_line(center_x, center_y, minute_x, minute_y, width=int(clock_radius * 0.03), fill=hand_color, tags="hands", capstyle=tk.ROUND)

    # Draw second hand (slim, modern)
    second_angle = math.radians(seconds * 6)
    second_x = center_x + (clock_radius - 40) * math.sin(second_angle)
    second_y = center_y - (clock_radius - 40) * math.cos(second_angle)
    canvas.create_line(center_x, center_y, second_x, second_y, width=int(clock_radius * 0.02), fill=second_hand_color, tags="hands", capstyle=tk.ROUND)

    # Redraw every second
    root.after(1000, update_clock)

# Function to toggle "always on top" mode
def toggle_always_on_top():
    if always_on_top_var.get():
        root.wm_attributes("-topmost", True)
    else:
        root.wm_attributes("-topmost", False)

# Function to adjust clock size dynamically
def adjust_size(val):
    global clock_radius
    clock_radius = int(val)
    draw_clock_face()

# Function to choose clock color
def choose_color():
    global clock_color
    color = colorchooser.askcolor(title="Choose Clock Color")
    if color[1]:
        clock_color = color[1]
    draw_clock_face()

# Function to choose hand color
def choose_hand_color():
    global hand_color
    color = colorchooser.askcolor(title="Choose Hand Color")
    if color[1]:
        hand_color = color[1]
    draw_clock_face()

# Function to choose second hand color
def choose_second_hand_color():
    global second_hand_color
    color = colorchooser.askcolor(title="Choose Second Hand Color")
    if color[1]:
        second_hand_color = color[1]
    draw_clock_face()

# Function to open the settings window
def open_settings(event=None):
    settings_window = tk.Toplevel(root)
    settings_window.geometry("300x200")
    settings_window.title("Clock Settings")
    
    # Always on top checkbox
    always_on_top_check = tk.Checkbutton(settings_window, text="Always on Top", variable=always_on_top_var, command=toggle_always_on_top)
    always_on_top_check.pack(pady=10)

    # Size adjustment slider
    size_scale = tk.Scale(settings_window, from_=100, to=400, orient="horizontal", label="Adjust Clock Size", command=adjust_size)
    size_scale.set(clock_radius)
    size_scale.pack(pady=10)

    # Color selection buttons
    clock_color_button = tk.Button(settings_window, text="Clock Color", command=choose_color)
    clock_color_button.pack(pady=5)

    hand_color_button = tk.Button(settings_window, text="Hand Color", command=choose_hand_color)
    hand_color_button.pack(pady=5)

    second_hand_color_button = tk.Button(settings_window, text="Second Hand Color", command=choose_second_hand_color)
    second_hand_color_button.pack(pady=5)

# Variables for settings
always_on_top_var = tk.IntVar()

# Initial drawing of the clock face
draw_clock_face()

# Start updating the clock hands
update_clock()

# Run the Tkinter event loop
root.mainloop()
