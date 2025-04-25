# Use Python 3.11 slim base image
FROM python:3.11-slim

# Prevent prompts from apt and set up environment
ENV DEBIAN_FRONTEND=noninteractive 

# Install system dependencies for Chromium (Playwright)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libnss3 libatk1.0-0 libatk-bridge2.0-0 libcairo2 libcups2 libdrm2 libgbm1 \
    libglib2.0-0 libgtk-3-0 libpangocairo-1.0-0 libpango-1.0-0 libfontconfig1 \
    libxcomposite1 libxdamage1 libxext6 libxfixes3 libxrandr2 libxcursor1 \
    libxss1 libxtst6 libasound2 libexpat1 libdbus-1-3 libdbus-glib-1-2 libxi6 \
    libx11-xcb1 libxcb1 libxkbcommon0 libffi7 libssl1.1 fonts-liberation libfreetype6 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies (Streamlit & Playwright)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files into the image
COPY app.py .
COPY run_tests.py .
COPY setup.sh .
RUN chmod +x setup.sh

# Install Playwright browsers (Chromium) via the setup script
RUN ./setup.sh

# Expose Streamlit's default port (8501) and set Streamlit to use the Render port
EXPOSE 8501
CMD streamlit run app.py --server.port $PORT --server.address 0.0.0.0
