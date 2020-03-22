##### Navigation objects for each UDT that hold information on which faceplate tabs are available #####

# Note: Originally a "Nav" UDT was created to store this information.  Nav instances were nested in the process object UDT definitions.  That strategy was abandoned because subsequent changes to the Nav type definition deleted the configurations in the Nav instances.

class Main():
	def __init__(self, operator=True, maintenance=True, trends=True, diagnostics=True, alarms=True):
		self.operator=operator
		self.maintenance=maintenance
		self.trends=trends
		self.diagnostics=diagnostics
		self.alarms=alarms
	def getTabDict(self):
		return {
			'hasOperator':self.operator,
			'hasMaintenance':self.maintenance,
			'hasTrends':self.trends,
			'hasDiagnostics':self.diagnostics,
			'hasAlarms':self.alarms
		}

class Advanced():
	def __init__(self, maintenance=1, engineering=1, hmi=1, faults=1):
		self.maintenance=maintenance
		self.engineering=engineering
		self.hmi=hmi
		self.faults=faults
	def getPageCountDict(self):
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



### Nav object instances for each UDT

P_VSD = Nav(
	name='P_VSD',
	advanced=Advanced(
		engineering=5,
		faults=0
	)
)

P_ValveC = Nav(
	name='P_ValveC',
	main=Main(
		trends=False
	),
	advanced=Advanced(
		engineering=3,
		faults=0,
		maintenance=2
	)
)

P_ValveSO = Nav(
	name='P_ValveSO',
	main=Main(
		trends=False
	),
	advanced=Advanced(
		engineering=2,
		faults=0,
		maintenance=1
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

P_Perm = Nav(
	name='P_Perm',
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




def getNavObject(udtTypeName):
	navList = [P_VSD, P_PIDE, P_AIn, P_Intlk, P_Perm, P_CmdSrc, P_Gate, P_Alarm, P_ValveC, P_ValveSO]
	for obj in navList:
		if(obj.name==udtTypeName):
			return obj	
	
		