<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=220&section=header&text=CODTECH%20AI%20Internship&fontSize=60&fontAlignY=35&desc=Artificial%20Intelligence%20Implementations&descAlignY=55" />
  
  <br/><br/>
  
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=800&size=28&pause=1000&color=F72DD2&center=true&vCenter=true&width=600&lines=Natural+Language+Processing;Speech+Recognition;Computer+Vision;Large+Language+Models+(GPT-2)" alt="Typing SVG" />
  </a>
  
  <br/>
  
  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" />
    <img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" />
    <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
  </p>
</div>

<br/>

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Telescope.png" alt="Telescope" width="30" height="30" /> About The Project

This repository serves as a spectacular showcase of modern Python-based AI implementations. The architecture is cleanly divided into **4 independent modules** that solve sophisticated real-world technical problems using state-of-the-art libraries.

<img src="https://raw.githubusercontent.com/aaronward/aaronward/master/assets/images/rainbow-divider.gif" width="100%"/>

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Wrench.png" alt="Wrench" width="30" height="30" /> Module Breakdowns & Outputs

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Memo.png" alt="Memo" width="35" height="35" /> Task 1: Text Summarization Tool
Designed a performant tool that leverages **Hugging Face's `distilbart-cnn-12-6` transformers** architecture to dynamically summarize large blocks of raw text without losing critical context.

<details open>
<summary><b>🔥 View Output Snapshot</b></summary>
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

<img src="https://raw.githubusercontent.com/aaronward/aaronward/master/assets/images/rainbow-divider.gif" width="100%"/>

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Studio%20Microphone.png" alt="Microphone" width="35" height="35" /> Task 2: Speech Recognition Engine
An automated audio-transcription script built with the **SpeechRecognition API**. It ingests standard `.wav` files and natively converts voice vectors into highly accurate string transcripts!

<details open>
<summary><b>🔥 View Output Snapshot</b></summary>
<br/>

```yaml
=== CODTECH Task 2: Speech Recognition System ===
Reading audio file: sample_audio.wav
Recognizing speech...

--- Transcription ---
"Artificial intelligence and machine learning are creating a wonderful future."
```
</details>

<img src="https://raw.githubusercontent.com/aaronward/aaronward/master/assets/images/rainbow-divider.gif" width="100%"/>

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Artist%20Palette.png" alt="Palette" width="35" height="35" /> Task 3: Neural Style Transfer Interface
A stunning display of Deep Learning and Computer Vision using **TensorFlow Hub's Magenta** models. It flawlessly transcribes the visual style of a famous painting onto a real-world photograph using spatial transformations.

<details open>
<summary><b>🔥 View Output Snapshot</b></summary>
<br/>

| Base Photograph (`content.jpg`) | Artistic Style (`style.jpg`) | Output Render (`stylized_output.jpg`) |
| :---: | :---: | :---: |
| <img src="content.jpg" width="220"/> | <img src="style.jpg" width="220"/> | <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Placeholder_image.svg/1200px-Placeholder_image.svg.png" width="220"/> |
*(Note: A stylized output is generated dynamically upon execution)*

<br/>

```yaml
=== CODTECH Task 3: Neural Style Transfer ===
Loading TF Hub Arbitrary Image Stylization model...
Applying style transfer (this might take a moment)...
Stylized image successfully saved to stylized_output.jpg
```
</details>

<img src="https://raw.githubusercontent.com/aaronward/aaronward/master/assets/images/rainbow-divider.gif" width="100%"/>

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Robot.png" alt="Robot" width="35" height="35" /> Task 4: GPT-2 Generative Text Model
Harnesses the massive generative power of **OpenAI's GPT-2 via HuggingFace**. Given a custom text prompt, the script maps the contextual embeddings and hallucinates realistic human-readable continuations.

<details open>
<summary><b>🔥 View Output Snapshot</b></summary>
<br/>

```yaml
=== CODTECH Task 4: Generative Text Model ===
Loading text generation model (GPT-2)...
Generating continuation for: 'The future of artificial intelligence in healthcare is'...

--- Generated Text ---
The future of artificial intelligence in healthcare is bright. Rapid innovations in predictive diagnostics and automated robotic surgeries are expected to radically decrease hospital wait times, providing significantly faster and more accurate care to millions around the globe.
```
</details>

<img src="https://raw.githubusercontent.com/aaronward/aaronward/master/assets/images/rainbow-divider.gif" width="100%"/>

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Rocket.png" alt="Rocket" width="30" height="30" /> Quick Start Guide

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
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" />
</div>
