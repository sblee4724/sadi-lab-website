# Expands YAML anchors/merge keys in tools/cms-config.src.yml into public/admin/config.yml
# (Decap CMS does not accept merge keys or extra top-level keys). Run after editing the source file.
import yaml, os
here=os.path.dirname(__file__)
d=yaml.safe_load(open(os.path.join(here,'cms-config.src.yml')))
d={k:v for k,v in d.items() if not k.startswith('x-')}
class NoAlias(yaml.SafeDumper):
    def ignore_aliases(self, data): return True
out="# Generated from tools/cms-config.src.yml by tools/build_cms_config.py — edit the source file.\n"
out+=yaml.dump(d,Dumper=NoAlias,allow_unicode=True,sort_keys=False,width=200)
open(os.path.join(here,'..','public','admin','config.yml'),'w').write(out)
print('ok', out.count('\n'),'lines')
