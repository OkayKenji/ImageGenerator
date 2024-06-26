from PIL import Image, ImageDraw, ImageFont
import csv
import threading
import time 

a = time.time()
print("Starting a: ",a)


# Load a TrueType font
font_size = 50
font_path = "./ArialNarrow7-9YJ9n.ttf"  # Update with the path to your .ttf file
font = ImageFont.truetype(font_path, font_size)

# Function to process a portion of the CSV data and generate images
def generate_images(start_index, rows):
    for index, row in enumerate(rows, start=start_index):
        text = row[0]
        print(f"Thread {start_index // len(rows)}: Generating image: {text}")

        # Create a blank image with white background
        width, height = 2500, 200
        image = Image.new('RGB', (width, height), 'white')
        draw = ImageDraw.Draw(image)

        # Text position
        text_position = (10, 80)

        # Draw the text on the image
        draw.text(text_position, text, font=font, fill="black")

        # Save the image to a file
        image.save(f'./images/{index}.png', 'PNG')

# Read CSV file into a list of rows
with open('text.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    rows = list(csv_reader)

num_threads = 50
rows_per_thread = len(rows) // num_threads

# Create and start threads
threads = []
for i in range(num_threads):
    start_index = i * rows_per_thread
    end_index = (i + 1) * rows_per_thread if i != num_threads - 1 else len(rows)
    thread = threading.Thread(target=generate_images, args=(start_index, rows[start_index:end_index]))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads have finished execution")
b = time.time()
print("Done in ",b-a)

