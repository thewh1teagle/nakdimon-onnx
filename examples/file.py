"""
Please download nakdimon model before execute

wget https://github.com/thewh1teagle/nakdimon-onnx/releases/download/v0.1.0/nakdimon.onnx
python usage.py input.txt output.txt
"""

from nakdimon_onnx import Nakdimon
import sys

input = sys.argv[1]
output = sys.argv[2]

nakdimon = Nakdimon("nakdimon.onnx")
text = open(input, "r", encoding="utf-8").read()
dotted_text = nakdimon.compute(text)
with open(output, "w", encoding="utf-8") as f:
    f.write(dotted_text)
