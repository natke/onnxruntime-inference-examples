import json
from pathlib import Path
import torch
import torchvision.transforms as T
from torchvision.io import read_image
from show import show
from model import Predictor

torch.manual_seed(1)
device = 'cuda' if torch.cuda.is_available() else 'cpu'

dog1 = read_image(str(Path('dog1.jpg')))
dog2 = read_image(str(Path('dog2.jpg')))

dog1 = dog1.to(device)
dog2 = dog2.to(device)

transforms = torch.nn.Sequential(
    T.CenterCrop(370),
)

cropped_dog1 = transforms(dog1)
cropped_dog2 = transforms(dog2)

show([cropped_dog1, cropped_dog2])

predictor = Predictor().to(device)
scripted_predictor = torch.jit.script(predictor).to(device)
batch = torch.stack([cropped_dog1, cropped_dog2]).to(device)
res = predictor(batch)
res_scripted = scripted_predictor(batch)

with open(Path('imagenet_class_index.json')) as labels_file:
    labels = json.load(labels_file)

for i, (pred, pred_scripted) in enumerate(zip(res, res_scripted)):
    assert pred == pred_scripted
    print(f"Prediction for Dog {i + 1}: {labels[str(pred.item())]}")
