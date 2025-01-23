# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "nakdimon==0.1.2",
#     "onnx==1.17.0",
#     "tf2onnx==1.16.0",
# ]
# ///

"""
wget https://github.com/elazarg/nakdimon/raw/refs/heads/master/nakdimon/Nakdimon.h5
uv run scripts/export.py
"""

from nakdimon.predict import load_cached_model
import tf2onnx
import onnx

model = load_cached_model("Nakdimon.h5")
onnx_model, _ = tf2onnx.convert.from_keras(model)
onnx.save(onnx_model, "nakdimon.onnx")
