from PIL import Image, ImageDraw

# Settings for the chargebar dimensions and animation
width, height = 200, 50         # Overall image dimensions for horizontal bar
bar_padding = 4                 # Padding around the inner bar
num_frames = 20                 # Number of frames for the animation
duration = 100                  # Frame duration in milliseconds

# List to hold each frame
frames = []

# Standard horizontal loading bar
for i in range(num_frames + 1):
    # Create a new image with transparent background (RGBA)
    im = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)
    
    # Draw the outer border for the chargebar
    border_color = "black"
    draw.rectangle([0, 0, width-1, height-1], outline=border_color, width=2)
    
    # Calculate the current fill width for the inner bar
    max_fill_width = width - 2 * bar_padding
    fill_width = int(max_fill_width * (i / num_frames))
    
    # Choose a fill color
    fill_color = "green"
    
    # Draw the charge fill bar with calculated width
    draw.rectangle([bar_padding, bar_padding, bar_padding + fill_width, height - bar_padding], fill=fill_color)
    
    # Append the current frame to the list
    frames.append(im)

# Save frames as an animated GIF, looping forever
frames[0].save("chargebar_horizontal.gif", save_all=True, append_images=frames[1:], duration=duration, loop=0)

# Vertical loading bar
frames = []
width, height = 50, 200  # Overall image dimensions for vertical bar

for i in range(num_frames + 1):
    # Create a new image with transparent background (RGBA)
    im = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)
    
    # Draw the outer border for the chargebar
    border_color = "black"
    draw.rectangle([0, 0, width-1, height-1], outline=border_color, width=2)
    
    # Calculate the current fill height for the inner bar
    max_fill_height = height - 2 * bar_padding
    fill_height = int(max_fill_height * (i / num_frames))
    
    # Choose a fill color
    fill_color = "blue"
    
    # Draw the charge fill bar with calculated height
    draw.rectangle([bar_padding, height - bar_padding - fill_height, width - bar_padding, height - bar_padding], fill=fill_color)
    
    # Append the current frame to the list
    frames.append(im)

# Save frames as an animated GIF, looping forever
frames[0].save("chargebar_vertical.gif", save_all=True, append_images=frames[1:], duration=duration, loop=0)

# Circular loading bar
frames = []
diameter = 100  # Diameter of the circular bar
center = diameter // 2
radius = center - bar_padding

for i in range(num_frames + 1):
    # Create a new image with transparent background (RGBA)
    im = Image.new("RGBA", (diameter, diameter), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)
    
    # Draw the outer border for the chargebar
    border_color = "black"
    draw.ellipse([bar_padding, bar_padding, diameter - bar_padding, diameter - bar_padding], outline=border_color, width=2)
    
    # Calculate the current fill angle for the inner circle
    end_angle = int(360 * (i / num_frames))
    
    # Choose a fill color
    fill_color = "red"
    
    # Draw the charge fill arc with calculated angle
    draw.pieslice([bar_padding, bar_padding, diameter - bar_padding, diameter - bar_padding], start=0, end=end_angle, fill=fill_color)
    
    # Append the current frame to the list
    frames.append(im)

# Save frames as an animated GIF, looping forever
frames[0].save("chargebar_circular.gif", save_all=True, append_images=frames[1:], duration=duration, loop=0)

# Bricks building a wall and completing a charge bar
frames = []
width, height = 300, 100  # Overall image dimensions for the brick animation
brick_width, brick_height = 50, 20  # Dimensions of each brick
bar_width, bar_height = 200, 20  # Dimensions of the charge bar
bar_x, bar_y = (width - bar_width) // 2, height - bar_height - 10  # Position of the charge bar

def draw_brick(draw, x, y, width, height):
    # Draw a simple brick shape
    draw.rectangle([x, y, x + width, y + height], fill="brown", outline="black")

for i in range(num_frames + 1):
    # Create a new image with transparent background (RGBA)
    im = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)
    
    # Draw the outer border for the chargebar
    border_color = "black"
    draw.rectangle([bar_x, bar_y, bar_x + bar_width, bar_y + bar_height], outline=border_color, width=2)
    
    # Calculate the current fill width for the inner bar
    max_fill_width = bar_width - 2 * bar_padding
    fill_width = int(max_fill_width * (i / num_frames))
    
    # Choose a fill color
    fill_color = "green"
    
    # Draw the charge fill bar with calculated width
    draw.rectangle([bar_x + bar_padding, bar_y + bar_padding, bar_x + bar_padding + fill_width, bar_y + bar_height - bar_padding], fill=fill_color)
    
    # Calculate the number of bricks to draw
    num_bricks = int((i / num_frames) * (bar_width // brick_width))
    
    # Draw the bricks
    for j in range(num_bricks):
        brick_x = bar_x + bar_padding + (j * brick_width)
        brick_y = bar_y - brick_height - 5  # Position the bricks above the charge bar
        draw_brick(draw, brick_x, brick_y, brick_width, brick_height)
    
    # Append the current frame to the list
    frames.append(im)

# Save frames as an animated GIF, looping forever
frames[0].save("brick_chargebar.gif", save_all=True, append_images=frames[1:], duration=duration, loop=0)

print("Animated chargebar GIFs created as chargebar_horizontal.gif, chargebar_vertical.gif, chargebar_circular.gif, and brick_chargebar.gif")