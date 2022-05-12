import torch
print("torch_version:",torch.__version__)
print("cuda_version:",torch.version.cuda)
print("cudnn_version:",torch.backends.cudnn.version())
print("----------------------------------")
flag = torch.cuda.is_available()
print(flag)

print("device_count:",torch.cuda.device_count())
ngpu= 1
# Decide which device we want to run on
device = torch.device("cuda:0" if (torch.cuda.is_available() and ngpu > 0) else "cpu")
print(device)
print("device_name:",torch.cuda.get_device_name(0))
print(torch.rand(3,3).cuda())
