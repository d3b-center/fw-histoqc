#!/usr/bin/python3
import subprocess
import os
from flywheel_gear_toolkit import GearToolkitContext
from parse_config import parse_config
import flywheel_gear_toolkit
import flywheel
import re
from run_level import get_hierarchy

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
new_acquisition = ses.add_acquisition(label=f'{names}-histoqc')
for files in os.listdir(out):
 print(files)
 new_acquisition.upload_file(f'{out}/{files}')
  
 






