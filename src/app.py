import uuid
import streamlit as st
from pdf2image import convert_from_bytes
import io
from color_swap import convert_black_to_color

st.set_page_config(page_title="Music Sheet Colorizer", layout="centered")

st.title("PDF Print without black converter")
st.write("Upload your document and choose a substitue color for black ink.")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")
target_color = st.color_picker("Pick your ink color", "#000035")

if uploaded_file is not None:
    if st.button("Convert PDF"):
        with st.spinner("Processing pages... (this may take a moment)"):
            try:
                file_bytes = uploaded_file.read()

                pages = convert_from_bytes(file_bytes)

                processed_pages = convert_black_to_color(
                    pages, target_color=target_color
                )

                output_pdf = io.BytesIO()
                if processed_pages:
                    processed_pages[0].save(
                        output_pdf,
                        "PDF",
                        resolution=150.0,
                        save_all=True,
                        append_images=processed_pages[1:],
                    )
                    output_pdf.seek(0)

                    st.success("Conversion complete!")

                    random_string = str(uuid.uuid4()).replace('-', '')[:8] # just to diversify output names
                    st.download_button(
                        label="⬇️ Download Converted PDF",
                        data=output_pdf,
                        file_name=f"converted_pdf_{random_string}.pdf",
                        mime="application/pdf",
                    )

            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.info("Ensure you have poppler installed: `brew install poppler`")
