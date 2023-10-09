import subprocess as sp
import json
from json_stream_parser import load_iter
import glob
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import os.path as path

def run(a):
  return sp.Popen(a, shell=True, text=True, stdout=sp.PIPE).stdout

with open("token", "r") as tfile:
  token = tfile.read().strip()

results = defaultdict(dict)

def download(cmd, name):
  for p in load_iter(run(cmd)):
    results[str(name)].update({"pipelines": p})

with ThreadPoolExecutor(max_workers=100) as executor:
  for obj in load_iter(run("jq -f all.jq submissions/*.json")):
    cmd = f"curl 'https://gitlab.com/api/v4/projects/{obj['uri']}/pipelines?private_token={token}' | jq length"
    results[obj["name"]].update(obj)
    executor.submit(lambda: download(cmd, obj['name']))

for f in glob.glob("cs330e-collatz-tests/*TestCollatz.out"):
  name = path.basename(f).split("-TestCollatz.out")[0]
  for obj in load_iter(run("gawk -f process_test.awk " + f)):
    for k,v in obj.items():
      results[str(name)][k] = v

for f in glob.glob("cs330e-collatz-tests/*RunCollatz.out"):
  name = path.basename(f).split("-RunCollatz.out")[0]
  for p in load_iter(run("wc -l " + f + " | awk '{ print $1 }'")):
    results[str(name)]["ntests"] = p

with open("output.json", "w") as f:
  json.dump(results, f, indent="  ")
