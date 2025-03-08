import torch
import os

# 1. Print PyTorch version and module file path
print("PyTorch version:", torch.__version__)
print("Torch module file:", torch.__file__)

# 2. Print the build configuration details (CUDA, cuDNN, etc.)
print("\nPyTorch Build Configuration:")
print(torch.__config__.show())

# 3. Print the torch._C file path and list its dynamic dependencies
print("\ntorch._C file:", torch._C.__file__)
print("\nDynamic dependencies of torch._C:")
!ldd $(python -c "import torch._C; print(torch._C.__file__)")

# 4. Display PyTorch package metadata using pip
print("\nPip show torch:")
!pip show torch

# 5. Print the LD_LIBRARY_PATH environment variable
print("\nLD_LIBRARY_PATH:", os.environ.get("LD_LIBRARY_PATH"))
