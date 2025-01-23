# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "nakdimon==0.1.2",
# ]
# ///

"""
wget https://github.com/elazarg/nakdimon/raw/refs/heads/master/nakdimon/Nakdimon.h5
uv run scripts/inference.py
"""

from nakdimon import diacritize

result = diacritize("שלום עולם!")
print(result)
