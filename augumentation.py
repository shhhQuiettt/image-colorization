import torchvision.transforms as transforms


augumentation_pipeline = transforms.Compose(
    [
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(10),
        transforms.RandomAdjustSharpness(2),
    ]
)
