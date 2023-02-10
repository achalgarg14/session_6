import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader
from torch.optim import Adam
import numpy as np
from torch.optim.lr_scheduler import StepLR
from tqdm import tqdm

import model_class
from model_class import Net
import train_model
from train_model import train
import test_model
from test_model import test

def train_test_model(trainloader, testloader, norm_type='BN', EPOCHS=20, dropout=0.1, lr=0.001, lambda_l1 = 0.001, device='cpu'):

  train_losses = []
  test_losses = []
  train_acc = []
  test_acc = []
  wrong_predictions = []
  model =  Net(dropout, norm_type).to(device)
  optimizer = Adam(model.parameters(), lr=lr)
  scheduler = StepLR(optimizer, step_size=40, gamma=0.1)
  count = 0
  
  for epoch in range(EPOCHS):
    print("EPOCH:", epoch)
    train(model, device, trainloader, optimizer, epoch, train_losses, train_acc, lambda_l1)
    scheduler.step()
    eval_test_acc = test(model, device, testloader, test_losses, test_acc, epoch)
    if(eval_test_acc > 85):
        count+=1
        if count >=2:
          break
  
  model.eval()
  for images, labels in testloader:
    images, labels = images.to(device), labels.to(device)
    output = model(images)
    pred = output.argmax(dim=1, keepdim=True)  # get the index of the max log-probability
    match = pred.eq(labels.view_as(pred)).to('cpu').numpy()
    for j, i in enumerate(match):
      if(i == False):
        wrong_predictions.append((images[j], pred[j].item(), labels[j].item()))

  print(f'Total Number of incorrectly predicted images by model type {norm_type} is {len(wrong_predictions)}')
  return model, train_losses, test_losses, train_acc, test_acc, wrong_predictions