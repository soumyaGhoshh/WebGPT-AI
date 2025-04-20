# WebGPT-Lite – Mini Research AI Agent

This AI Agent fetches and summarizes real-world knowledge using Wikipedia + Hugging Face. Great for quick research!

## Example

**Input**: "Climate change impact on agriculture"

**Output**: A 3-5 line summary of the effects of climate change on crop yield, rainfall, and food security.

## Stack
- Wikipedia API
- Hugging Face Transformers (`distilbart-cnn-12-6`)
- Streamlit

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
