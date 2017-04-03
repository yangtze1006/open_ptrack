## *********************************************************
## 
## File autogenerated for the swissranger_camera package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 233, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 259, 'description': 'ROS tf frame of reference, resolved with tf_prefix unless absolute.', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'frame_id', 'edit_method': '', 'default': 'camera', 'level': 3, 'min': '', 'type': 'str'}, {'srcline': 259, 'description': 'Camera calibration URL for this video_mode (uncalibrated if null).', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'camera_info_url', 'edit_method': '', 'default': '', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 259, 'description': 'Auto exposure control state.', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'auto_exposure', 'edit_method': "{'enum_description': 'Feature control states', 'enum': [{'srcline': 54, 'description': 'Use fixed value', 'srcfile': '/home/zhao/workspace/ros/catkin/src/open_ptrack/swissranger_camera/cfg/SwissRanger.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Off'}, {'srcline': 55, 'description': 'Camera sets continuously', 'srcfile': '/home/zhao/workspace/ros/catkin/src/open_ptrack/swissranger_camera/cfg/SwissRanger.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Auto'}]}", 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 259, 'description': 'integration_time control.', 'max': 255, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'integration_time', 'edit_method': '', 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 259, 'description': 'amplitude_threshold control.', 'max': 65535, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'amp_threshold', 'edit_method': '', 'default': -1, 'level': 0, 'min': -1, 'type': 'int'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])    
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

SwissRanger_Off = 0
SwissRanger_Auto = 1