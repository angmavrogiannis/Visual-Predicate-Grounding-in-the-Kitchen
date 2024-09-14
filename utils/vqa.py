import torch
from PIL import Image
from lavis.models import load_model_and_preprocess
import argparse

# setup device to use
device = torch.device("cuda") if torch.cuda.is_available() else "cpu"

model, vis_processors, _ = load_model_and_preprocess(
    name="blip2_t5", model_type="pretrain_flant5xl", is_eval=True, device=device
)
parser = argparse.ArgumentParser(description='Simple Visual Question Answering (VQA)')
parser.add_argument('-p','--prompt', help='prompt (visual query)', required=True)
parser.add_argument('-i','--input_image', help='Path of input image (optional)', required=False)
args = parser.parse_args()

raw_image = Image.open(args.input_image).convert('RGB')   
image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
answer = model.generate({"image": image, "prompt": args.prompt})
with open("vqa.txt", "w") as f:
    f.write(answer[0])