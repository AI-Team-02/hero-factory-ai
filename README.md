# 🧟 hero-factory-ai

Follow these steps to set up the environment for your ComfyUI workflow:

1️⃣ **Create a new virtual environment**:
    
```
conda create -n [프로젝트명] python=3.10
conda activate [프로젝트명]

```
    
2️⃣ **가상환경 위에서 PyTorch with CUDA support 설치**:
- Visit the PyTorch website (https://pytorch.org/get-started/locally/) and get the correct installation command for your system. It should look something like this:
    
```
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

```
    
3️⃣ **가상환경 생성 후 가상환경 위에서 필요한 프로그램 설치**:
- Navigate to the directory containing your `requirements.txt` file and run:
    
```
pip install -r requirements.txt

```
    
4️⃣ **사용하고싶은 모델 다운로드 후 각 디렉토리에 맞게 넣어준다.**
- ex) `ComfyUI/models/controlnet/` directory: control_v11p_sd15_lineart_fp16.safetensors

5️⃣ **필요한 커스텀 노드 다운로드** :
    
- For each custom node, clone its repository into the `custom_nodes` directory:
- 또는, ComfyUI-Manager를 통해 간편하게 다운로드 가능
    
```
cd ComfyUI/custom_nodes
git clone [해당 커스텀 노드 git url]

```
    
6️⃣ **checkpoint model 다운로드**:
- `ComfyUI/models/checkpoints/` directory.

7️⃣ **Run ComfyUI**:
- Navigate to your ComfyUI directory and run:

```
python main.py

```

## 🦜 Custom Nodes

이 프로젝트를 실행하기 위해서는 다음 커스텀 노드들이 필요합니다.

* [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) (#1)
* [ComfyUI Impact Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack) (#2)
* [ComfyUI Inspire Pack](https://github.com/ltdrdata/ComfyUI-Inspire-Pack) (#3)
* [ComfyUI's ControlNet Auxiliary Preprocessors](https://github.com/Fannovel16/comfyui_controlnet_aux) (#8)
* [ComfyUI Custom Nodes AlekPet](https://github.com/AlekPet/ComfyUI_Custom_Nodes_AlekPet) (#60)
* [ComfyUI Custom Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts) (#62)
* [Comfyroll Studio](https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes) (#80)
* [KJNodes for ComfyUI](https://github.com/kijai/ComfyUI-KJNodes) (#252)
* [Crystools](https://github.com/crystian/ComfyUI-Crystools) (#492)
* [ComfyUI-tbox](https://github.com/ai-shizuka/ComfyUI-tbox) (#1200)

## 🐬 Models
이 프로젝트를 실행하기 위해서는 다음 모델들이 필요합니다.

### Checkpoints
* [Juggernaut XL - Lightning V9](https://civitai.com/models/133005?modelVersionId=357609) ([Download](https://civitai.com/api/download/models/357609?type=Model&format=SafeTensor&size=full&fp=fp16))

### ControlNet
* [controlnet-scribble-sdxl-1.0](https://huggingface.co/xinsir/controlnet-scribble-sdxl-1.0/tree/main) ([Download](https://huggingface.co/xinsir/controlnet-scribble-sdxl-1.0/blob/main/diffusion_pytorch_model.safetensors))

### Loras
* [Pixel Art XL](https://civitai.com/models/120096/pixel-art-xl) ([Download](https://civitai.com/api/download/models/135931?type=Model&format=SafeTensor))
* [【SDXL】Game Icon | Diablo Style | Dataset](https://civitai.com/models/209703/sdxlgame-icon-or-diablo-style-or-dataset) ([Download](https://civitai.com/api/download/models/236202?type=Model&format=SafeTensor))

