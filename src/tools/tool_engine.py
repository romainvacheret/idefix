from abc import ABC, abstractmethod
from typing import Final

class ToolEngine(ABC):
	TOOLS_FOLDER: Final = 'tools'
	PROJECTS_FOLDER: Final = 'projects'

	def __init__(self) -> None:
		self.base_command = None	
		self.tool_folder = None

	def _extract_parameters_if_present(self, 
			param_names: list[str],
			parameters: dict) -> list[str]:
		return [f'{param} {parameters[param]}' for param in param_names]

	# TODO Improve error management
	@abstractmethod
	def compile_program(self, path: str, command: str) -> bool:
		pass

	# TODO Improve error management
	@abstractmethod
	def run(self, parameters: dict) -> bool:
		pass
