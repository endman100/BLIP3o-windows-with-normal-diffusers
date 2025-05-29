from setuptools import setup, find_packages

setup(
    name="blip3o",
    version="0.1.0.1",
    packages=find_packages(),
    include_package_data=True,  # 啟用包含 MANIFEST.in 中指定的檔案
    package_data={
        "blip3o": [
            "model/*",          # 包含 model 資料夾中的所有檔案
            "model/*/*",        # 包含 model 資料夾中的子資料夾
        ]
    },
    install_requires=[
        "tokenizers",
        "sentencepiece",
        "shortuuid",
        "torch",
        "torchvision",
        "torchaudio",
        "transformers==4.51.3",
        "accelerate",
        "peft",
        "bitsandbytes",
        "pydantic",
        "markdown2",
        "numpy",
        "scikit-learn",
        "gradio",
        "gradio_client",
        "requests",
        "httpx",
        "uvicorn",
        "fastapi",
        "einops",
        "einops-exts",
        "timm",
        "ftfy",
        "diffusers",
        "datasets",
        "tabulate",
        "ninja",
        "qwen_vl_utils",
        "huggingface_hub",
    ],
)