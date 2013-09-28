#!/usr/bin/env python

from icloudtabslib import iCloudTabsReader

icloud = iCloudTabsReader()

for tab in icloud.tabs:

	print "%s <%s> (%s)" % (tab['title'], tab['url'], tab['device'])
	
