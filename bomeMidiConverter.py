from ObjectContainer import ObjectContainer as oc
from objects import get_details


def get_output(name):
    return oc._get(name)['Note']

def get_start_val(name):
    return oc._get(name)['Start Val']

def init_daw(daws):
    for daw in daws:
        pass


# oc._add("preset_counter", 0)
# def get_preset_num():
#     result = oc._get("preset_counter")
#     oc._set("preset_counter", result + 1)
#     return result
# 
# def create_init():
#     result = []
#     result.append(
#         create_preset(
#             name   = "Initialize",
#             active = True,
#             psi    = False          # PresetSwitchIgnore
#         )
#     )
# 
#     print_gv = []
#     gv = oc._get("global_vars")
#     for g in gv:
#         if g['Taken']:
#             print_gv.append(g)
#     options = []
#     for g in print_gv:
#         options.append(
#             "//{}".format(g['Taken'])
#         )
#         options.append(
#             "{}={}".format(g['Var'], g['Value'])
#         )
#     options.append("")
#     options = convert_options(options)
# 
# 
#     result.append(
#         create_translator(0, 'global_vals', "", "", options)
#     )
# 
#     return "".join(result)
# 
# def convert_options(options):
#     result = []
#     for o in options:
#         result.append(convert_option(o))
#     result = "".join(result)
#     return result
# 
# def convert_option(o):
#     result = ""
#     if o[:2] == "//":
#         # comment
#         result = "label{}__cmt>{}".format(
#             to_hex(len(o)+6), o
#         )
#     elif o[:2] == "if":
#         pass
#     elif "=" in o:
#         result = o
#     return result
# 
# import re
# def to_hex(num):
#     result = re.sub('x', '0', hex(num))
#     return result
# 
# def create_preset(name, active, psi):
#     num = get_preset_num()
# 
#     if type(active) == bool: active = int(active)
#     if type(psi)    == bool: psi    = int(psi)
# 
#     result = [
#         "[Preset.{}]".format(num),
#         "Name={}".format(name),
#         "Active={}".format(active),
#         "PresetSwitchIgnore={}".format(psi),
#         ""
#     ]
#     return "\n".join(result)
# 
# def create_translator(num, name, incoming, outgoing, options):
#     result = [
#         "Name{}={}".format(num, name),
#         "Incoming{}={}".format(num, incoming),
#         "Outgoing{}={}".format(num, outgoing),
#         "Options{}={}".format(num, options),
#         ""
#     ]
#     return "\n".join(result)
