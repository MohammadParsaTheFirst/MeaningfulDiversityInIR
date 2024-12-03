import torch 
import faiss

x = torch.cuda.is_available()
print(x)
print(torch.__version__)
print(faiss.__version__)