from bertalign import Bertalign
import pandas as pd
import io

# open your file, and make it the source text
with open('1984_2_EN.txt', 'r') as f:
  # read the file
  src = f.read()

# open your file, and make it the target text
with open('1984_2_NL.txt', 'r') as f:
  # read the file
  tgt = f.read()