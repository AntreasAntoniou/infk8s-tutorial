import torch
import torch.nn as nn
import torch.nn.functional as F

from rich import print
import fire

def run_experiment(seed: int):
    
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    
    a = torch.randn(10, 512)
    b = torch.randn(512, 10)
    
    c = torch.matmul(a, b)
    
    print(c)

if __name__ == "__main__":
    fire.Fire(run_experiment)
    
    