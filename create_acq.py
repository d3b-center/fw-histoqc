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

names=(os.environ["bashvar"])
print(names)
out=(os.environ["output"])
print(out)
[fw,d] = parse_config(flywheel_gear_toolkit.GearToolkitContext())
fi=flywheel.Client(str(fw))
hierarchy = get_hierarchy(flywheel_gear_toolkit.GearToolkitContext().client,d)
print(hierarchy)
sub_label = hierarchy['subject_label']
ses_label = hierarchy['session_label']
project_label = hierarchy['project_label']
group_name = hierarchy['group']
ses=fi.lookup(f'{group_name}/{project_label}/{sub_label}/{ses_label}')
acq_id =get_acq(fi,group_name, project_label,sub_label,ses_label,names)
print(acq_id)
rowcount = 0
for row in open(f'/flywheel/v0/output_temp/results.tsv'):
  rowcount+= 1
  if rowcount == 6:
   keys=(row.split('\t'))
  elif rowcount ==7:
   values =(row.split('\t'))
   for s,b in zip(keys, values):
      print(f'{s}:{b}') 
      body=flywheel.models.info_update_input.InfoUpdateInput(set={s:b})
      fi.modify_acquisition_file_info(acq_id,names,body)
new_acquisition = ses.add_acquisition(label=f'{names}-histoqc')
for files in os.listdir(out):
 print(files)
 new_acquisition.upload_file(f'{out}/{files}')
 






