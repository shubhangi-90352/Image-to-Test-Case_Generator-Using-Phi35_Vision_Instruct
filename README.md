# Describe_Test_Case_Using_PHI35_Vision_Instruct
The Image-to-Test-Case Generator is a web application built using Flask and Azure services and Open Source Multimodal LLM PHI3.5_vision_instruct. 

# Flask Application
app.py: The main Flask application file. It contains routes and functions for handling image uploads and interactions with Azure services.
# Azure Integration
Blob Storage: Functions to upload images to Azure Blob Storage and retrieve their URLs
# Prompting Strategy
## Overview
The application uses a structured prompting strategy to guide Azure’s  PHI3.5_vision_instruct in generating detailed image test cases. <br>

The strategy includes:

### System Message: 
The system message sets the context for the AI model, instructing it to act as an assistant for generating test cases based on images.

### User Message: The user message includes:

A request for generating test cases with a specific format (Description, Pre-conditions, Testing Steps, Expected Result).
The image URL and any additional context provided by the user.


# Model Summary
Phi-3.5-vision is a lightweight, state-of-the-art open multimodal model built upon datasets which include - synthetic data and filtered publicly available websites - with a focus on very high-quality, reasoning dense data both on text and vision. The model belongs to the Phi-3 model family, and the multimodal version comes with 128K context length (in tokens) it can support. The model underwent a rigorous enhancement process, incorporating both supervised fine-tuning and direct preference optimization to ensure precise instruction adherence and robust safety measures.

https://huggingface.co/microsoft/Phi-3.5-vision-instruct

# Test Case
<img src="https://github.com/user-attachments/assets/8be3c44e-efa7-46f8-9ae0-5a3463171780" width="300">
<img src="https://github.com/user-attachments/assets/8aea909d-0930-4fce-b7bd-94a0c01119f2" width="300">
<img src="https://github.com/user-attachments/assets/b31c4601-736f-427c-864d-c17c4aec4a70" width="300">
<img src="https://github.com/user-attachments/assets/5fa108f6-e039-45b4-975a-43fb665a482c" width="300">
<img src="https://github.com/user-attachments/assets/f8a5a69d-1257-4f96-93f1-9c4b0cb4132b" width="300">
<img src="https://github.com/user-attachments/assets/6b5ba6e0-1e3d-4461-8798-cbc504a5a5a7" width="300">
<img src="https://github.com/user-attachments/assets/eb2d919e-719a-46d8-a1c0-dcf7b3742e07" width="300">
<img src="https://github.com/user-attachments/assets/a2a021d1-f440-4dfb-b188-1508f69b837f" width="300">

# Results
<img src="https://github.com/user-attachments/assets/2e22860d-60f8-437b-8f93-a9b929d668d4" width="800">
<img src="https://github.com/user-attachments/assets/d51e50a1-a651-4db9-a9d5-c863f9d9927e" width="800">
<img src="https://github.com/user-attachments/assets/c971695d-d053-44d1-a231-dcd1ca1290b1" width="800">










