import os
import subprocess
import plistlib

class iCloudTabsReader:

	#
	# Populates self.tabs with a list of dictionaries.
	# Each dictionary contains the 'title' and 'url' of a Safari tab,
	# as well as the 'name' of the associated device.
	#
	def __init__(self, input=None):
		
		if input == None:
			# ~/Library/SyncedPreferences/com.apple.SafariServices.plist is similar
			input = os.path.expanduser('~/Library/SyncedPreferences/com.apple.Safari.plist');
		
		# Use plutil to convert binary plist to XML.
		pipe = subprocess.Popen(('/usr/bin/plutil', '-convert', 'xml1', '-o', '-', input), shell=False, stdout=subprocess.PIPE).stdout
		xml = plistlib.readPlist(pipe)
		pipe.close()

		self.tabs = []
		
		for device_id in xml['values']:
		
			device = xml['values'][device_id]['value']
			name = device.get('DeviceName')
			tabs = device.get('Tabs')
			
			if tabs != None:
				for tab in tabs:
					self.tabs.append({'title': tab['Title'], 'url': tab['URL'], 'device': name})
