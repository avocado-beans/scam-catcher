import google.generativeai as genai
import time

def answer(key, prompt, image):
    genai.configure(api_key=key)
    sample_file = genai.upload_file(path=image, display_name="Question")
    file = genai.get_file(name=sample_file.name)
    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
    generation_config = genai.GenerationConfig(temperature=0.0)
    response = model.generate_content([prompt, sample_file], generation_config=generation_config)
    return(response.text)
