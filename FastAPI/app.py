# -*- coding: utf-8 -*-
from fastapi import FastAPI, HTTPException, File, UploadFile, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import json
import httpx
import asyncio
import os
from uuid import uuid4
import io
import logging

# 환경변수 처리
load_dotenv()

# 환경변수에서 API 키 가져오기
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

COMFY_UI_URL = "http://127.0.0.1:8188"

WORKFLOW_PATH = os.path.abspath("../ComfyUI/workflow/2D_game_object_gemini_api.json")
OUTPUT_DIR = os.path.abspath("../ComfyUI/output")
UPLOAD_DIR = os.path.abspath("../ComfyUI/upload")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def queue_prompt(prompt_data):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{COMFY_UI_URL}/prompt", json={"prompt": prompt_data})
        response.raise_for_status()
        return response.json()

async def get_image(prompt_id):
    while True:  # 무한 루프로 변경
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{COMFY_UI_URL}/history/{prompt_id}")
            response.raise_for_status()
            data = response.json()
            
            if prompt_id in data and "outputs" in data[prompt_id]:
                return data[prompt_id]["outputs"]
        await asyncio.sleep(1)  # 1초 대기 후 다시 확인

@app.post("/generate-image")
async def generate_image(image: UploadFile = File(...), prompt: str = Form(...)):
    try:
        logger.info(f"Received request - prompt: {prompt}")

        image_content = await image.read()
        image_path = os.path.join(UPLOAD_DIR, f"{uuid4()}.png")
        with open(image_path, "wb") as f:
            f.write(image_content)
        logger.debug(f"Saved uploaded image to {image_path}")

        with io.open(WORKFLOW_PATH, 'r', encoding='utf-8') as file:
            workflow = json.load(file)
        
        workflow["195"]["inputs"]["prompt"] = prompt
        workflow["186"]["inputs"]["image"] = image_path
        workflow["188"]["inputs"]["api_key"] = GEMINI_API_KEY

        result = await queue_prompt(workflow)
        prompt_id = result["prompt_id"]
        logger.info(f"Prompt queued with ID: {prompt_id}")
        
        output = await get_image(prompt_id)
        
        # 생성된 이미지 파일명 직접 가져오기 (Save Image)
        generated_image_filename = output["187"]["images"][0]["filename"]
        
        image_path = os.path.join(OUTPUT_DIR, generated_image_filename)
        
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Generated image file not found: {image_path}")
        
        logger.info(f"Generated image found at {image_path}")
        
        return FileResponse(image_path, media_type="image/png", filename=generated_image_filename)
    
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting the server")
    uvicorn.run(app, host="0.0.0.0", port=28000)