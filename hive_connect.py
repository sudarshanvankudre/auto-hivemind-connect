import json
import urllib.request
import argparse

parser = argparse.ArgumentParser()
data = json.load(urllib.request.urlopen("https://www.ocf.berkeley.edu/~hkn/hivemind/data/latest.json"))


def compare_machine(machine):
    avg_load = sum(data["data"][machine]["load_avgs"]) / len(data["data"][machine]["load_avgs"])
    num_users = len(data["data"][machine]["users"])
    return avg_load, num_users


machines = filter(lambda s: s.startswith("hive") and "load_avgs" in data["data"][s], data["data"])
lowest_load_machine = min(machines, key=compare_machine)




