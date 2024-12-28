import torch 
import faiss

x = torch.cuda.is_available()
print(x)
print(torch.__version__)
print(faiss.__version__)



# python test.py --conf_path configs/example_config.yaml



# ctrl+shift+p => Git: Add Remote
# ctrl+shift+p => Git: Push
# gir add .
# git commit -m ""
# git push origin main