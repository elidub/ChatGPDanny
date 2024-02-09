# ChatGPDanny

## Demo
https://github.com/elidub/ChatGPDanny/assets/62380460/f96b11fd-2466-40fd-b097-0c03d5a047b9

## Intallation
```bash
conda create -y -n chatgpdanny python=3.10 
conda activate chatgpdanny
pip install -r requirements.txt
```

## Proproces data
```bash
python chatgpdanny/preprocess_chat.py
```

## How to run
First, save an OpenAPI key in `store/openai_api_key.txt` (I know that this is not good practice). 

To chat, run:
```
python chatgptdanny/run.py
```
