#
# Copyright (C) 2015 by YOUR NAME HERE
#
#    This file is part of RoboComp
#
#    RoboComp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RoboComp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
#

import sys, os, Ice

ROBOCOMP = ''
try:
	ROBOCOMP = os.environ['ROBOCOMP']
except:
	print '$ROBOCOMP environment variable not set, using the default value /opt/robocomp'
	ROBOCOMP = '/opt/robocomp'
if len(ROBOCOMP)<1:
	print 'ROBOCOMP environment variable not set! Exiting.'
	sys.exit()
	

preStr = "-I"+ROBOCOMP+"/interfaces/ --all "+ROBOCOMP+"/interfaces/"

Ice.loadSlice(preStr+"rcdns.ice")
from RoboCompRCDNS import *

class rcdnsI(rcdns):
	def __init__(self, worker):
		self.worker = worker

	def getAllComps(self, c):
		return self.worker.getAllComps()
	def getAllCompsHost(self, host, c):
		return self.worker.getAllCompsHost(host)
	def getComponentId(self, port, host, c):
		return self.worker.getComponentId(port, host)
	def getComponentHostNameByPort(self, port, c):
		return self.worker.getComponentHostNameByPort(port)
	def giveMePort(self, idComp, hostInfo, c):
		return self.worker.giveMePort(idComp, hostInfo)
	def getComponentPort(self, idComp, host, c):
		return self.worker.getComponentPort(idComp, host)
	def getComponentHostNameById(self, idComp, c):
		return self.worker.getComponentHostNameById(idComp)




