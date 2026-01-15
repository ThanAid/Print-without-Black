# 🎵 Print Without Black

If your printer cannot print using black then you are in the right place!


**Convert your black & white sheet music (or documents) to Dark Blue to bypass a broken black ink cartridge.**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://print-without-black.streamlit.app/)

## 🚀 Live Demo
You don't need to install anything. Use the app directly in your browser:
**[https://print-without-black.streamlit.app/](https://print-without-black.streamlit.app/)**

---

## 🧐 Why?
If your printer's **Black (K)** cartridge is empty or clogged, but your **Color (CMY)** cartridges works, you can't print standard documents.
This tool converts the black pixels in a PDF to a **Deep Dark Blue (`#000035`)** or a color of choice. This forces the printer to not use black ink.

---

## 🛠 Run Locally with Docker
If you prefer to run the app on your own machine, you can use Docker. This handles all system dependencies (like Poppler) automatically.

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

### Quick Start
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/print-without-black.git](https://github.com/YOUR_USERNAME/print-without-black.git)
    cd print-without-black
    ```

2.  **Run with Docker Compose:**
    ```bash
    docker-compose up --build
    ```

3.  **Open in Browser:**
    Go to [http://localhost:8501](http://localhost:8501)


### 👀 PS I just have a broken printer :)
