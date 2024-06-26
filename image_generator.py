from PIL import Image, ImageDraw, ImageFont
import io
import csv

# Load a TrueType font
font_size = 50
font_path = "./ArialNarrow7-9YJ9n.ttf"  # Update with the path to your .ttf file
font = ImageFont.truetype(font_path, font_size)

with open('text.csv', 'r') as csvfile:
  csv_reader = csv.reader(csvfile)
  
  for index, row in enumerate(csv_reader):
    text = row[0]
    print("Generating image: ",text)
    

    # Create a blank image with white background
    width, height = 2000, 200 
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    
    # text position
    text_position = (10, 80) 

    # Draw the text on the image
    draw.text(text_position, text, font=font, fill="black") 

    # Save the imageS
    s = io.BytesIO()
    image.save(s, format='PNG')
    in_memory_file = s.getvalue()
    image.save(f'./images/{index}.png', 'PNG')
