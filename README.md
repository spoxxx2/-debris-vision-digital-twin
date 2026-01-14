# 📊 debris-vision-digital-twin

## 🚀 Project Overview
Hardwired AI vision system using **Hybrid YOLOv12 + Vision Transformer (ViT)** to categorize debris and generate **Digital Twin** logs for the circular economy.

## 🏷️ 4-Level Taxonomy
1. **Material:** (Polymer, Ferrous Metal, Cellulose, etc.)
2. **Sub-Type:** (PET #1, Aluminum, etc.)
3. **Condition:** (Soiled, Crushed, Intact, Wet)
4. **Disposal:** (Circular Economy, Incineration, Compost)

## 🔮 50-Year Digital Twin Forecast
Metadata includes `environmental_impact_score` and `digital_twin_forecast` (Worth/Danger/Appearance in 2076).

## 📥 Loading the Data
\`\`\`python
from datasets import load_dataset
dataset = load_dataset("spoxxx2/-debris-vision-digital-twin")
\`\`\`
