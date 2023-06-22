import fitz  # PyMuPDF
from PIL import Image

def take_screenshot(pdf_path, output_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Iterate over each page of the PDF
    for page_number in range(pdf_document.page_count):
        # Get the current page
        page = pdf_document.load_page(page_number)

        # Render the page as an image
        pix = page.get_pixmap()
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Save the image as a screenshot
        screenshot_path = f"{output_path}/page_{page_number + 1}.png"
        image.save(screenshot_path)

        print(f"Screenshot saved: {screenshot_path}")

    # Close the PDF document
    pdf_document.close()

# Specify the path to your PDF file
pdf_file_path = "C:/Users/Никита/Desktop/jjj/29.05.2023_S.pdf"

# Specify the output directory for the screenshots
output_directory = "C:/Users/Никита/Desktop/jjj"

# Call the function to take screenshots of the PDF pages
take_screenshot(pdf_file_path, output_directory)