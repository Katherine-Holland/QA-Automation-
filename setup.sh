#!/bin/bash

# Install system dependencies required for Chromium
apt-get update && apt-get install -y \
  libnss3 \
  libatk-bridge2.0-0 \
  libxcomposite1 \
  libxdamage1 \
  libxrandr2 \
  libgbm1 \
  libgtk-3-0 \
  libgtk-4-1 \
  libgraphene-1.0-0 \
  libgstreamer-gl1.0-0 \
  libgstreamer-plugins-bad1.0-0 \
  libavif15 \
  libenchant-2-2 \
  libsecret-1-0 \
  libmanette-0.2-0 \
  libgles2 \
  libasound2 \
  wget \
  curl \
  unzip \
  && rm -rf /var/lib/apt/lists/*

# Install Playwright with Chromium and all required dependencies
python -m playwright install --with-deps
