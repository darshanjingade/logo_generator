from PIL import Image, ImageDraw, ImageFont

# Create an image (transparent background)
width, height = 200, 100
image = Image.new("RGBA", (width, height), (255, 255, 255, 0))

draw = ImageDraw.Draw(image)

# Choose font and size (you can download a font and use its path)
# On Windows, you might find fonts in C:\Windows\Fonts\
try:
    font = ImageFont.truetype("arialbd.ttf", 80)  # Arial Bold, fallback if available
except:
    font = ImageFont.load_default()

# Text color and shadow
text = "DJ"
text_color = (30, 144, 255)  # Dodger Blue
shadow_color = (0, 0, 0, 150)  # semi-transparent black shadow

# Position text in the center with shadow effect
x, y = 20, 5

# Draw shadow
draw.text((x+2, y+2), text, font=font, fill=shadow_color)
# Draw main text
draw.text((x, y), text, font=font, fill=text_color)

# Optional: draw a rounded rectangle background (white with some transparency)
# Uncomment if you want a background box
# from PIL import ImageFilter
# bg_color = (255, 255, 255, 200)
# rect_x0, rect_y0, rect_x1, rect_y1 = 5, 5, width - 5, height - 5
# draw.rounded_rectangle([rect_x0, rect_y0, rect_x1, rect_y1], radius=20, fill=bg_color)

# Save logo
image.save("dj_logo.png")

print("Logo saved as dj_logo.png")
