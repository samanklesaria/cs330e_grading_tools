from json_stream_parser import load_iter
import json
import os
import sys
from collections import defaultdict

final = defaultdict(dict)

with open(sys.argv[1], "r") as f1:
  for obj in load_iter(f1):
    final[obj['name']].update(obj)

with open(sys.argv[2], "r") as f2:
  for obj in load_iter(f2):
    final[obj['name']].update(obj)

with open("output.json", "w") as f3:
  json.dump(final, f3, indent="  ")
