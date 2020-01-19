##### Navigation objects for each UDT that hold information on which faceplate tabs are available #####

class Main():
	def __init__(self, operator=True, maintenance=True, trends=True, diagnostics=True, alarms=True):
		self.operator=operator
		self.maintenance=maintenance
		self.trends=trends
		self.diagnostics=diagnostics
		self.alarms=alarms
	def getHiddenTabs(self):
		return {
			'hideOperator':self.operator==False,
			'hideMaintenance':self.maintenance==False,
			'hideTrends':self.trends==False,
			'hideDiagnostics':self.diagnostics==False,
			'hideAlarms':self.alarms==False
		}


class Advanced():
	def __init__(self, maintenance=1, engineering=1, hmi=1, faults=1):
		self.maintenance=maintenance
		self.engineering=engineering
		self.hmi=hmi
		self.faults=faults
	def getPageCounts(self):
		return {
			'maintenancePages':self.maintenance,
			'engineeringPages':self.engineering,
			'hmiPages':self.hmi,
			'faultsPages':self.faults
		}



class Nav():
	def __init__(self, name='',main=Main(), advanced=Advanced()):
		self.name=name
		self.main=main
		self.advanced=advanced




P_VSD = Nav(
	name='P_VSD',
	advanced=Advanced(
		engineering=5,
		faults=0
	)
)

P_PIDE = Nav(
	name='P_PIDE',
	advanced=Advanced(
		engineering=6,
		faults=2,
		maintenance=6
	)
)

P_AIn = Nav(
	name='P_AIn',
	advanced=Advanced(
		maintenance=0,
		faults=0
	)
)

P_Intlk = Nav(
	name='P_Intlk',
	main=Main(
		trends=False,
		diagnostics=False,
		alarms=False
	),
	advanced=Advanced(
		faults=0,
		maintenance=0,
		engineering=2
	)
)

P_CmdSrc = Nav(
	name='P_CmdSrc',
	main=Main(
		trends=False,
		diagnostics=False,
		alarms=False
	),
	advanced=Advanced(
		maintenance=0,
		faults=0,
		hmi=0,
		engineering=3
	)
)

P_Gate = Nav(
	name='P_Gate',
	main=Main(
		trends=False,
		diagnostics=False,
		maintenance=False,
		alarms=False
	),
	advanced=Advanced(
		maintenance=0,
		faults=0,
		hmi=0,
		engineering=0
	)
)

P_Alarm = Nav(
	name='P_Alarm',
	main=Main(
		trends=False,
		diagnostics=False,
		alarms=False
	),
	advanced=Advanced(
		maintenance=0,
		faults=0
	)
)


navList = [P_VSD, P_PIDE, P_AIn, P_Intlk, P_CmdSrc, P_Gate, P_Alarm]
		