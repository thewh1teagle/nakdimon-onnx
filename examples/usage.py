"""
Please download nakdimon model before execute

wget https://github.com/thewh1teagle/nakdimon-onnx/releases/download/v0.1.0/nakdimon.onnx
python usage.py
"""

from nakdimon_onnx import Nakdimon

nakdimon = Nakdimon("nakdimon.onnx")
text = "שלום עולם!"
dotted_text = nakdimon.compute(text)
print(dotted_text)
