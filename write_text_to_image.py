import pandas as pd
import math
from PIL import Image, ImageDraw, ImageFont

def write_text_to_image(excel_file, image_file):
  """Writes the text from each cell in the Excel file to an image file.

  Args:
    excel_file: The path to the Excel file.
    image_file: The path to the image file.
  """
  for i in range(9):
    cardWidth = 450
    cardHeight = 628
    columns = 4
    font_size = 35

    
    # Read the Excel file into a Pandas DataFrame.
    df = pd.read_excel(excel_file, sheet_name = i)
    
    # Open the image file.
    image = Image.new('1', (cardWidth * min(len(df.index), columns), math.ceil(len(df.index) / columns) * cardHeight))

    # Create a drawing object for the image.
    draw = ImageDraw.Draw(image)

    # Get the font.
    font = ImageFont.truetype("arial.ttf", font_size)
    # Iterate over the DataFrame rows.
    for j, row in enumerate(df.iterrows()):
      # Get the cell text.
      text = str(row[1].values[0])
      for k, value in enumerate(row[1].values):
        # Write the text to the image.
        #print(str(type(value)) + " " + str(value))
        if type(value) == str or not(math.isnan(value)):
          draw.text(((j%columns) * cardWidth, int(row[0]/columns) * cardHeight + k * font_size), str(value), 1, font=font)

    # Save the image.
    new_file = image_file + str(i) + '.png'
    #f = open(new_file, "x")
    image.save(new_file)


if __name__ == "__main__":
  # Get the Excel file path.
  excel_file = 'C:\\Users\\rathy\\Downloads\\witch hunt decks.xlsx'

  # Get the image file path.
  image_file = 'C:\\Users\\rathy\\Pictures\\witch-hunt\\'

  # Write the text from the Excel file to the image file.
  write_text_to_image(excel_file, image_file)

  print("Text successfully written to image.")
