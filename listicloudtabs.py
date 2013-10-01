#!/usr/bin/env python

# Run to print the current iCloud Tabs list in `title <url> (device)` format.

from icloudtabslib import iCloudTabsReader

icloud = iCloudTabsReader()

for tab in icloud.tabs:

	print "%s <%s> (%s)" % (tab['title'], tab['url'], tab['device'])
	
