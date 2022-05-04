from abc import ABC, abstractmethod

class ServerWrapper(ABC):
	@abstractmethod
	def serve(self):
		pass