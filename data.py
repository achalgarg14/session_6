import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import numpy as  np
import albumentations as A
from albumentations.pytorch import ToTensorV2

def default_dataset():
  transform = transforms.Compose(
    [transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

  trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                        download=True, transform=transform)
  trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                          shuffle=True, num_workers=2)

  testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                       download=True, transform=transform)
  testloader = torch.utils.data.DataLoader(testset, batch_size=4,
                                         shuffle=False, num_workers=2)
  return trainloader, trainset



class cifar_10(torchvision.datasets.CIFAR10):
    def __init__(self, root="./data", train=True, download=True, transform=None):
        super().__init__(root=root, train=train, download=download, transform=transform)

    def __getitem__(self, index):
        image, label = self.data[index], self.targets[index]

        if self.transform is not None:
            transformed = self.transform(image=image)
            image = transformed["image"]

        return image, label


def transform_params(mean, std):
  horizontal_p= 0.2
  rotate_limit= 15
  shiftscalerotate_p= 0.25
  num_holes= 1
  cutout_prob= 0.5
  max_height = 16 # half of max height (32)
  max_width = 16 # half of max width (32)

  transform_train = A.Compose(
    [A.HorizontalFlip(p=horizontal_p),
     A.ShiftScaleRotate(shift_limit=0.1, scale_limit=0.1, rotate_limit=rotate_limit, p=shiftscalerotate_p),
     A.CoarseDropout(max_holes=num_holes,min_holes = 1, max_height=max_height, max_width=max_width, 
              p=cutout_prob,fill_value=tuple([x * 255.0 for x in mean]),
              min_height=max_height, min_width=max_width, mask_fill_value = None),
     A.Normalize(mean = mean, std = std, max_pixel_value=255, always_apply = True),
     ToTensorV2()
    ])
  
  transform_valid = A.Compose(
    [
     A.Normalize(
            mean=mean,
            std=std,
            max_pixel_value=255,
        ),
     ToTensorV2()
    ])
  return transform_train, transform_valid


def transformed_dataset(transform_train,transform_valid):
  trainset = cifar_10(root='./data', train=True, download=True, transform=transform_train)
  trainloader = torch.utils.data.DataLoader(trainset, batch_size=128, shuffle=True, num_workers=2)
  testset = cifar_10(root='./data', train=False, download=True, transform=transform_valid)
  testloader = torch.utils.data.DataLoader(testset, batch_size=128, shuffle=False, num_workers=2)
  return trainset,trainloader,testset,testloader


