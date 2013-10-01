# iCloud Tabs Reader

A very simple Python class to get the current list of iCloud Tabs known to your Mac. The list does not update instantaneously as you browse, but usually seems to catch up within a few seconds.

## Installation

	sudo python setup.py install

## Usage

In Python:

	from icloudtablibs import iCloudTabsReader
	iCloudTabsReader().tabs

The `tabs` member of `iCloudTabsReader()` is a list of current iCloud Tabs. Each tab is represented as a dict with three properties: `title`, `url`, and `device` (the name of the device on which that tab is open).
