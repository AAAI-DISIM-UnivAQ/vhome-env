import glob
import sys
import os

workspace_path = os.getcwd() + "/virtualhome/src"

sys.path.append(workspace_path)

from virtualhome.simulation.unity_simulator.comm_unity import UnityCommunication

# For GNU/Linux
# exec_file = 'linux_exec/linux_exec.v2.3.0.x86_64'

# For MacOS
# exec_file = 'macos_exec/macos_exec.v2.3.0.app/Contents/MacOS/VirtualHome'

exec_file = 'linux_exec/linux_exec.v2.3.0.x86_64'

assert os.path.isfile(exec_file)

mode = 'auto'  # auto / manual

if mode == 'auto':

    file_names = glob.glob(exec_file)
    if len(file_names) > 0:
        file_name = file_names[0]
        comm = UnityCommunication(file_name=file_name,
                                  port="8082",
                                  x_display="0")
    else:
        print("Error: executable path not found.")
else:
    comm = UnityCommunication()
    print(comm)
