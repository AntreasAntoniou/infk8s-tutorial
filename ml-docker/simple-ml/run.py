import fire
import torch
import torch.nn as nn
import torch.nn.functional as F
from rich import print


def run_experiment(seed: int):
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)

    a = torch.randn(10, 512)
    b = torch.randn(512, 10)

    c = torch.matmul(a, b)

    print(
        f"Shape of c: {c.shape}, mean value: {c.mean()}, std value: {c.std()}, min value: {c.min()}, max value: {c.max()}"
    )


if __name__ == "__main__":
    fire.Fire(run_experiment)
