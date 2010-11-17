import sys,os

if sys.platform=="win32":
	import win32pdh
	import win32pdhquery
	import win32pdhutil
	import _winreg

# Parse the registry to find the localized perf counter name 
def pdhTranslateEnglishCounter (counter):
	key = _winreg.OpenKey (_winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Perflib\009")
	strings = _winreg.QueryValueEx (key, 'Counter')[0]
	for i in range(0,len(strings),2):
		if counter == strings[i+1]:
			return win32pdh.LookupPerfNameByIndex (None, int(strings[i]))
	return counter

def cpuCount():
	"""Returns the number of CPUs in the system"""
	num = 1
	if sys.platform == 'win32':
		try:
			num = int(os.environ['NUMBER_OF_PROCESSORS'])
		except (ValueError, KeyError):
			pass
	elif sys.platform == 'darwin':
		try:
			num = int(os.popen('sysctl -n hw.ncpu').read())
		except ValueError:
			pass
	else:
		try:
			num = os.sysconf('SC_NPROCESSORS_ONLN')
		except (ValueError, OSError, AttributeError):
			pass

	return num

class HostCPU:
	"""This class returns the per CPU"""
#	def __init__(self):
#		if sys.platform=="win32":
#			self.base = win32pdh.OpenQuery()
#			self.Counters = []
#			cpucount = cpuCount()
#			for cpuid in range(0,cpucount):
#				self.Counters.append (win32pdh.AddCounter(self.base, win32pdh.MakeCounterPath((None, pdhTranslateEnglishCounter ("Processor"),str(cpuid),None, -1, pdhTranslateEnglishCounter ("% Processor Time")))))
#				#self.Counters.append (win32pdh.AddCounter(self.base, win32pdh.MakeCounterPath((None, "Processor",str(cpuid),None, -1, "% Processor Time"))))
#			win32pdh.CollectQueryData(self.base)
	
	def getUsage(self):
		''' Return a list with the usage of each CPU '''
#		if sys.platform=="win32":
#			result = []
#			win32pdh.CollectQueryData(self.base)
#			for counter in self.Counters:
#				try:
#					load = win32pdh.GetFormattedCounterValue(counter,win32pdh.PDH_FMT_DOUBLE)[1]
#				except:
#					load = 0
#					pass
#				result.append (load)
#			return result 
#		else:
#			result = []
#			for cpuid in range(0,cpucount):			
#				result.append (0)
		return [0]
