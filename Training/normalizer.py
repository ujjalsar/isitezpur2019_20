# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 17:50:19 2019

@author: gupta
"""

import ruamel_yaml as yaml
import json

"""
declaring some constants
"""
(SCANS, INCIDENTS, AUDITS) = ("scans", "incidents", "audits")
job_types = [SCANS, INCIDENTS, AUDITS]

job_template_map = {SCANS:"scans.yaml", 
                    INCIDENTS:"incidents.yaml", 
                    AUDITS:"audits.yaml"}


data["info"]["nested1"]["high"] = 121
outdata["einfo"]["nested_first"]["high"] = 121


class Normalizer(object):
    def __init__(self, job_type, raw_data): #, elk_input_data):
        self.yamldata = self.load_yaml( job_template_map.get(job_type, None) )
        self.raw_data = raw_data
        #self.elk_input_data = elk_input_data
        
    def lint_json(self, data):
        jsonobj = json.loads(json.dumps(data))
        print(json.dumps(jsonobj,indent=2))
    
    def load_yaml(self, yaml_file="example.yaml"):
        if not yaml_file:
            return None
        yaml_data = None
        with open(yaml_file, 'r') as fp:
            try:
                yaml_data = yaml.safe_load(fp)
            except yaml.YAMLError as exc:
                print(exc)
        return yaml_data
    
    def load_json(self, json_file="scan_data.json"):
        with open(json_file) as fp:
            jobj = json.load(fp)
            print(yaml.dump(jobj))

    def get_elk_input(self):
        #
        pass

"""
selected items to modify
selected items to 
modification
mapping
modified attributes
changed attributes
selected items to push to elk for scan, incidents, audits
selected
expected
prefered
elk_pref_scan_dataset
expected input mapping
raw data
pref data scan, incidents, audits
pref template scan, incidents, audits
pref mapping scan, incidents, audits
"""


def main():
    print("main func called")
    #yamldata = load_yaml("example.yaml")
    #print(yamldata["info"]["data1"])

if __name__ == "__main__":
    main()

