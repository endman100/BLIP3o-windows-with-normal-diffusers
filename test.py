from qwen_vl_utils import process_vision_info
from blip3o.model.builder import load_pretrained_model
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoProcessor
import sys
import os
from PIL import Image
import torch
print(torch.__version__)
print(torch.cuda.is_available())

tokenizer, multi_model, _ = load_pretrained_model("BLIP3o/BLIP3o-Model-8B")

image_path = "./test_image/text to image_00031_.jpeg"
img = Image.open(image_path).convert("RGB")


processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct")
messages = [{
    "role": "user",
    "content": [
        {"type": "image", "image": img}, #Image.Image
        {"type": "text", "text": "Describe this image in detail."}, # str
    ],
}]

text_prompt_for_qwen = processor.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
image_inputs, video_inputs = process_vision_info(messages)
inputs = processor(
    text=[text_prompt_for_qwen],
    images=image_inputs,
    videos=video_inputs,
    padding=True,
    return_tensors="pt",
).to('cuda:0')
generated_ids = multi_model.generate(**inputs, max_new_tokens=1024)
input_token_len = inputs.input_ids.shape[1]
generated_ids_trimmed = generated_ids[:, input_token_len:]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True,
    clean_up_tokenization_spaces=False
)[0]

print(f"output_text: {output_text}")