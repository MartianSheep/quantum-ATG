import abc
import numpy as np
import qiskit.circuit.library as qGate
from qiskit.circuit.gate import Gate

class qatgFault(abc.ABC):
	def __init__(self, gateType, qubit, description = "A qATG Fault."):
		if not issubclass(gateType, Gate):
			raise TypeError('gateType must be one of qiskit.circuit.library')
		self.gateType = gateType
		if isinstance(qubit, int):
			qubit = [qubit]
		self.qubit = qubit
		self.description = description

	def __str__(self):
		return self.description

	def getGateType(self):
		return self.gateType

	def getQubit(self):
		return self.qubit

	@abc.abstractmethod
	def getOriginalGateParameters(self):
		return NotImplemented

	def getOriginalGate(self, qubit):
		return self.gateType(*self.getOriginalGateParameters())

	@abc.abstractmethod
	def getFaulty(self, parameters):
		return NotImplemented