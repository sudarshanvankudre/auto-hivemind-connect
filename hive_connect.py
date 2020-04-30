import json
import urllib.request
import os
import argparse

SUFFIX = ".berkeley.edu"

parser = argparse.ArgumentParser(description="Start ssh session with a UC Berkeley hivemind machine")
parser.add_argument("username", help="Your username. (Ex: cs000-aaa)")
args = parser.parse_args()
data = json.load(urllib.request.urlopen("https://www.ocf.berkeley.edu/~hkn/hivemind/data/latest.json"))


def compare_machine(machine):
    avg_load = sum(data["data"][machine]["load_avgs"]) / len(data["data"][machine]["load_avgs"])
    num_users = len(data["data"][machine]["users"])
    return avg_load, num_users


machines = filter(lambda s: s.startswith("hive") and "load_avgs" in data["data"][s], data["data"])
lowest_load_machine = min(machines, key=compare_machine)
command = "ssh -X {}@{}{}".format(args.username, lowest_load_machine, SUFFIX)
os.system(command)
