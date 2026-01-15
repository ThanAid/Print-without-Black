import argparse
from pdf2image import convert_from_path
from PIL import ImageOps


def convert_black_to_color(pages: list, target_color: str) -> list:
    processed_pages = []

    for i, page in enumerate(pages):
        print(f"  Converting page {i + 1}...")
        gray_image = page.convert("L")

        colored_page = ImageOps.colorize(gray_image, black=target_color, white="white")

        processed_pages.append(colored_page)

    return processed_pages


def convert_black_to_blue(input_pdf_path: str, output_pdf_path: str) -> None:
    print(f"Processing: {input_pdf_path}...")

    try:
        pages = convert_from_path(input_pdf_path)
    except Exception as e:
        print(f"Error reading PDF: {e}")
        print("Make sure you ran: 'brew install poppler'")
        return

    converted_pages = convert_black_to_color(pages, target_color="#000035")

    if converted_pages:
        print(f"Saving to {output_pdf_path}...")
        converted_pages[0].save(
            output_pdf_path,
            "PDF",
            resolution=150.0,
            save_all=True,
            append_images=converted_pages[1:],
        )
        print("Done!")
    else:
        print("No pages found.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert black PDF sheet music to dark blue."
    )

    parser.add_argument("input_file", help="Path to the source PDF file")
    parser.add_argument("output_file", help="Path where the new PDF will be saved")
    args = parser.parse_args()

    convert_black_to_blue(args.input_file, args.output_file)
