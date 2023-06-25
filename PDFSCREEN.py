import fitz  # PyMuPDF
from PIL import Image
from datetime import datetime,timedelta





def TODay():
    current_date = datetime.now()
    next_day = current_date + timedelta(days=0)
    formatted_date = next_day.strftime("%d.%m.%Y")
    file_name=(formatted_date +"_S.pdf")
    return file_name
def NEXT():
    current_date = datetime.now()
    next_day = current_date + timedelta(days=1)
    formatted_date = next_day.strftime("%d.%m.%Y")
    file_name=(formatted_date +"_S.pdf")
    return file_name

def take_screenshot_today():
    pdf_file_path = "C:/Users/Никита/Documents/GitHub/timetableBOT/"+TODay()
    output_directory = "C:/Users/Никита/Documents/GitHub/timetableBOT/TODAY"

    # Open the PDF file
    pdf_document = fitz.open(pdf_file_path)

    # Iterate over each page of the PDF
    for page_number in range(pdf_document.page_count):
        # Get the current page
        page = pdf_document.load_page(page_number)

        # Render the page as an image
        pix = page.get_pixmap()
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Save the image as a screenshot
        screenshot_path = f"{output_directory}/{TODay()}_{page_number + 1}.png"
        image.save(screenshot_path)

        print(f"Screenshot saved: {screenshot_path}")

    # Close the PDF document
    pdf_document.close()

# Specify the path to your PDF file


# Specify the output directory for the screenshots


# Call the function to take screenshots of the PDF pages
def take_screenshot_next():
    pdf_file_path = "C:/Users/Никита/Documents/GitHub/timetableBOT/"+NEXT()
    output_directory = "C:/Users/Никита/Documents/GitHub/timetableBOT/tomorrow"

    # Open the PDF file
    pdf_document = fitz.open(pdf_file_path)

    # Iterate over each page of the PDF
    for page_number in range(pdf_document.page_count):
        # Get the current page
        page = pdf_document.load_page(page_number)

        # Render the page as an image
        pix = page.get_pixmap()
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Save the image as a screenshot
        screenshot_path = f"{output_directory}/{TODay()}_{page_number + 1}.png"
        image.save(screenshot_path)

        print(f"Screenshot saved: {screenshot_path}")

    # Close the PDF document
    pdf_document.close()


