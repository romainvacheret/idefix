from os import getcwd
from os.path import join
from typing import Final, Union
from subprocess import run, DEVNULL, PIPE

from src.tools.tool_engine import ToolEngine

def _write_file(filename: str, content: str) -> None:
	with open(filename, 'w') as file:
		file.write(content)


class AstorEngine(ToolEngine):
	VALID_PARAMETERS: Final = ['-mode', # APR technique to use
		'-srcjavafolder', # projet source folder 
		'-srctestfolder', # projet test folder
		'-binjavafolder', # projet source .class files
		'-bintestfolder', # projet test .class files
		'-location', # project path
		'-dependencies'] # project dependencies folder

	def __init__(self):
		super().__init__()
		self.tool_folder = 'tools/astor'
		self.base_command = ['java', '-cp', 
			f'{join(getcwd(), self.tool_folder, "target/astor-*-jar-with-dependencies.jar")}',
			'fr.inria.main.evolution.AstorMain']

	def compile_program(self, path: str, command: Union[str, list[str]]=None) -> bool:
		if command is None:
			command = ['mvn', 'clean', 'compile', 'test', '-DskipTests']
		elif isinstance(command, str):
			command = command.split(' ')

		result = run(command, cwd=path, stdout=DEVNULL, stderr=PIPE)
		return result.stderr == b''

	def run(self, parameters: dict) -> bool:
		valid_parameters = {param: value for param, value in parameters.items() \
			if param in self.VALID_PARAMETERS}
		script_name = 'script.sh'
		# TODO change the parameters -> names
		command = self.base_command + self._extract_parameters_if_present(
			self.VALID_PARAMETERS,
			valid_parameters)
		command_as_string = ' '.join(command)

		# For some reason running the command from Python does not work
		# execute a script instead
		_write_file(script_name, command_as_string)
		run(['chmod', '777', script_name])

		result = run(['sh', script_name], stdout=DEVNULL, stderr=PIPE)

		return result.stderr == b''