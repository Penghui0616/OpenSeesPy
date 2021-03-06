import sys
import ctypes
import glob

# only work for 64 bit system
if sys.maxsize < 2**31:
    raise RuntimeError('64 bit system is required')

# platform dependent
if sys.platform.startswith('linux'):


    try:
        from openseespy.opensees.linux.opensees import *
    except:
        raise RuntimeError('Failed to import openseespy on Linux.')

elif sys.platform.startswith('win'):

    if sys.version_info[0] == 3 and sys.version_info[1] == 8:

        dll_path = ''
        for path in sys.path:
            if 'DLLs' in path:
                dll_path = path
                break
        ctypes.cdll.LoadLibrary(dll_path + '\\tcl86t.dll')

        try:
            from openseespy.opensees.win.opensees import *

        except:

            raise RuntimeError(
                'Failed to import openseespy on Windows for Python 3.8')

    else:
        raise RuntimeError(
            'Python version 3.8 is needed for Windows')

elif sys.platform.startswith('darwin'):

    if sys.version_info[0] == 3 and sys.version_info[1] == 8:
        try:
            from openseespy.opensees.mac.opensees import *
        except:
            raise RuntimeError('Failed to import, try use Python from HomeBrew')
    else:
        raise RuntimeError('Python version 3.8 is needed for Mac')


else:

    raise RuntimeError(sys.platform+' is not supported yet')
