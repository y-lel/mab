import fitz


def insert_stego_image_into_pdf(input_pdf, stego_image, output_pdf):
    doc = fitz.open(input_pdf)
    page = doc[0]

    # Smaller image + padding
    image_width = 60
    image_height = 60
    padding = 30

    page_width, page_height = page.rect.width, page.rect.height
    rect = fitz.Rect(
        page_width - image_width - padding,
        page_height - image_height - padding,
        page_width - padding,
        page_height - padding
    )

    page.insert_image(rect, filename=stego_image)
    doc.save(output_pdf)
    doc.close()
