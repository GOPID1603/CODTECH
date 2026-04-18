<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=CODTECH%20AI%20Internship&fontSize=50&fontAlignY=35&desc=Artificial%20Intelligence%20Implementations&descAlignY=55" />
  
  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" />
    <img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" />
    <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
  </p>
  
  <h3>An immersive suite of advanced Artificial Intelligence models encompassing Natural Language Processing, Computer Vision, and Speech Recognition.</h3>
</div>

<br/>

## 🎯 About The Project

This repository serves as a showcase of modern Python-based AI implementations. The architecture is cleanly divided into 4 independent modules that solve sophisticated real-world technical problems using state-of-the-art libraries.

---

## 🛠️ Module Breakdowns & Outputs

### 📝 Task 1: Text Summarization Tool
Designed a performant tool that leverages **Hugging Face's `distilbart-cnn-12-6` transformers** architecture to dynamically summarize large blocks of raw text.

<details open>
<summary><b>🖼️ View Output Snapshot</b></summary>
<br/>

```yaml
Loading summarization model...
Generating summary...

Original Text Length: 673 characters
---
Summary Length: 284 characters
Summary Text:
Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to intelligence displayed by animals and humans. AI applications include advanced web search engines, recommendation systems, understanding human speech, self-driving cars, and generative tools.
```
</details>

---

### 🎙️ Task 2: Speech Recognition Engine
An automated audio-transcription script built with the **SpeechRecognition API**. It ingests standard `.wav` files and converts voice vectors into highly accurate string transcripts!

<details open>
<summary><b>🖼️ View Output Snapshot</b></summary>
<br/>

```yaml
=== CODTECH Task 2: Speech Recognition System ===
Reading audio file: sample_audio.wav
Recognizing speech...

--- Transcription ---
"Artificial intelligence and machine learning are creating a wonderful future."
```
</details>

---

### 🎨 Task 3: Neural Style Transfer Interface
A stunning display of Deep Learning and Computer Vision using **TensorFlow Hub's Magenta** models. It flawlessly transcribes the visual style of a famous painting onto a real-world photograph using spatial transformations.

<details open>
<summary><b>🖼️ View Output Snapshot</b></summary>
<br/>

| Base Photograph (`content.jpg`) | Artistic Style (`style.jpg`) | Output Render (`stylized_output.jpg`) |
| :---: | :---: | :---: |
| <img src="content.jpg" width="250"/> | <img src="style.jpg" width="250"/> | <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Placeholder_image.svg/1200px-Placeholder_image.svg.png" width="250"/> |
*(Note: A stylized output is generated upon execution of the script)*

<br/>

```yaml
=== CODTECH Task 3: Neural Style Transfer ===
Loading TF Hub Arbitrary Image Stylization model...
Applying style transfer (this might take a moment)...
Stylized image successfully saved to stylized_output.jpg
```
</details>

---

### 🤖 Task 4: GPT-2 Generative Text Model
Harnesses the massive generative power of **OpenAI's GPT-2 via HuggingFace**. Given a custom text prompt, the script maps the contextual embeddings and hallucinates realistic human-readable continuations.

<details open>
<summary><b>🖼️ View Output Snapshot</b></summary>
<br/>

```yaml
=== CODTECH Task 4: Generative Text Model ===
Loading text generation model (GPT-2)...
Generating continuation for: 'The future of artificial intelligence in healthcare is'...

--- Generated Text ---
The future of artificial intelligence in healthcare is bright. Rapid innovations in predictive diagnostics and automated robotic surgeries are expected to radically decrease hospital wait times, providing significantly faster and more accurate care to millions around the globe.
```
</details>

---

## 💻 Quick Start Guide

**1. Clone the environment:**
```bash
git clone https://github.com/GOPID1603/CODTECH.git
cd CODTECH
```

**2. Install Dependencies:**
```bash
pip install -r requirements.txt
```

**3. Execution:**
```bash
python task1_text_summarization.py
```

<br/>
<div align="center">
  <b>✨ Coded & Configured for CODTECH ✨</b>
</div>
