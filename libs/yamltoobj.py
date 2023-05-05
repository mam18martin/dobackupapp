import yaml
class YamlToObj:
    def __init__(self, in_dict):
        
        if type(in_dict) == str:
            with open(in_dict) as f:
                in_dict = yaml.load(f, Loader=yaml.FullLoader)
        
        for key, val in in_dict.items():
            if isinstance(val, (list, tuple)):
               setattr(self, key, [YamlToObj(x) if isinstance(x, dict) else x for x in val])
            else:
               setattr(self, key, YamlToObj(val) if isinstance(val, dict) else val)

# Use like
# o = YamlToObj("config.yaml")
# p = o.credential
# print(p.user)
