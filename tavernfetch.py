import psutil
import platform


left = [
    "  ___________",
    " /__  ___/__/",
    "   / / / /_",
    "  / / / __/",
    " / / / /",
    "/_/ /_/"]
right = [
    "",
    "Tavernfetch 0.1",
    ""]

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_size2(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1000
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

uname = platform.uname()
right.append("System: " + uname.system)
right.append("Hostname: " + uname.node)
#right.append(f"Release: {uname.release}")
right.append("CPU: " + uname.processor + " (" + uname.machine + ")")

# number of cores
right.append("Physical cores: " + str(psutil.cpu_count(logical=False)))
right.append("Logical cores: " + str(psutil.cpu_count(logical=True)))
# CPU frequency
cpufreq = psutil.cpu_freq()
right.append("CPU Frequency: " + get_size2(cpufreq.current * 1000000, suffix='hz') + " (" + get_size(cpufreq.current * 1000000, suffix='hz') + ")")
right.append("")
# Memory Information
# get the memory details
svmem = psutil.virtual_memory()
right.append("Total RAM: " + get_size(svmem.total) + " (" + get_size2(svmem.total) + ")")
right.append("Empty RAM: " + get_size(svmem.available) + " (" + get_size2(svmem.available) + ")")
right.append("Non-empty RAM: " + get_size(svmem.used) + " (" + get_size2(svmem.used) + ")")
right.append("RAM usage: " + str(float(svmem.percent) / 100))
right.append("")
# get the swap memory details (if exists)
swap = psutil.swap_memory()
right.append("Total SWAP: " + get_size(swap.total) + " (" + get_size2(swap.total) + ")")
right.append("Empty SWAP: " + get_size(swap.free) + " (" + get_size2(swap.free) + ")")
right.append("Non-empty SWAP: " + get_size(swap.used) + " (" + get_size2(swap.used) + ")")
right.append("SWAP usage: " + str(float(swap.percent) / 100))

leftWidth = 0
for item in left:
    if(len(item) > leftWidth):
        leftWidth = len(item)

leftWidth += 3

for i in range(0, len(right)):
    right[i] = "\033[36m" + right[i] + "\033[0m"

newleft = []
for i in range(0, len(left)):
    newleft.append("")
    newleft[i] = "\033[33m" + left[i] + "\033[0m"

for i in range(0, max(len(left), len(right))):
    try:
        print(newleft[i] + " " * (leftWidth - len(left[i])) + right[i])
    except IndexError:
        if(len(left) > len(right)):
            print(left[i])
        else:
            print(" " * leftWidth + right[i])
