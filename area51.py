import psutil


def get_pid(task):
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'cmdline'])
        except psutil.NoSuchProcess:
            pass
        else:
            # E. g. : pinfo = {
            # 'cmdline': ['proceesB', "-r", "r_value0123"],
            # 'pid': 12345
            # }
            if task in pinfo['cmdline']:
                return pinfo['pid']
    return None


get_pid('py.exe')
