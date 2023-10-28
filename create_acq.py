#!/usr/bin/python3
import subprocess
import os
from flywheel_gear_toolkit import GearToolkitContext
from parse_config import parse_config
import flywheel_gear_toolkit
import flywheel
import re
from run_level import get_hierarchy
from run_level import get_acq

#get output path and slide name  from bash to python
slide_file_name =(os.environ["bashvar"])
out=(os.environ["output"])
print(out)

#get flywheel client using sdk
[fw,d] = parse_config(flywheel_gear_toolkit.GearToolkitContext())
fw=flywheel.Client(str(fw))

#get hierarchical flywheel data structure 
hierarchy = get_hierarchy(flywheel_gear_toolkit.GearToolkitContext().client,d)
sub_label = hierarchy['subject_label']
ses_label = hierarchy['session_label']
project_label = hierarchy['project_label']
group_name = hierarchy['group']
ses=fw.lookup(f'{group_name}/{project_label}/{sub_label}/{ses_label}')
#get acquisition id
acq_id =get_acq(fw,group_name, project_label,sub_label,ses_label, slide_file_name)
rowcount = 0

#parse result file to insert metadata to slide file
for row in open(f'/flywheel/v0/output_temp/results.tsv'):
  rowcount+= 1
  if rowcount == 6:
   keys=(row.split('\t'))
  elif rowcount ==7:
   values =(row.split('\t'))
   new_dict = {keys: values for keys,
   values in zip(keys, values)}
   body = flywheel.models.info_update_input.InfoUpdateInput(set={f'{slide_file_name} - histoqc':new_dict})
   fw.modify_acquisition_file_info(acq_id, slide_file_name,body)

#create new acq to move all the output files
new_acquisition = ses.add_acquisition(label=f'{slide_file_name} - histoqc')
for files in os.listdir(out):
 new_acquisition.upload_file(f'{out}/{files}')
 