from __future__ import annotations
from typing import NoReturn, Final
from os import getcwd
from os.path import join

from src.communication.server_wrapper import ServerWrapper
from src.utils.files import Path, convert_to_absolute_path, list_generated_variants

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from jsonrpc import JSONRPCResponseManager, dispatcher

SERVER_HOST: Final = '127.0.0.1'
SERVER_PORT: Final = 8080


def compile_program(engine, path, command) -> bool:
	path = convert_to_absolute_path([engine.PROJECTS_FOLDER, path])
	return engine.compile_program(path, command)


def _update_parameters(parameters: dict, project_folder_path: Path) -> dict:
	project_full_path = join(getcwd(), project_folder_path)
	parameters['-location'] = join(project_full_path, parameters['-location'])
	parameters['-dependencies'] = join(project_full_path, parameters['-dependencies'])
	
	return parameters
	

def run_analysis(engine: ToolEngine, parameters: dict) -> bool:
	# TODO: check if the compilation was successfull
	return engine.run(_update_parameters(parameters, engine.PROJECTS_FOLDER))


def list_diffs(output_folder: Path, project_name: str) -> list[dict]:
	path = join(output_folder, 'output_astor', f'AstorMain-{project_name}', 'src')
	print(path)
	return list_generated_variants(path)


class JsonRpcServerWrapper(ServerWrapper):
	def __init__(self, engine: ToolEngine) -> None:
		self._engine = engine

		@Request.application
		def application(request) -> Response:
			self._register_commands()
			reponse = JSONRPCResponseManager.handle(
				request.data, dispatcher)
			return Response(reponse.json, mimetype='application/json')

		self._application = application

	def _register_commands(self) -> None:
		dispatcher['ping'] = lambda x: x
		dispatcher['compile'] = lambda path, command: compile_program(
			self._engine, path, command)
		dispatcher['analyze'] = lambda parameters: run_analysis(
			self._engine, parameters)
		dispatcher['list-diffs'] = lambda project_name: list_diffs(
			self._engine.PROJECTS_FOLDER, project_name)

	def serve(self) -> NoReturn:
		run_simple(SERVER_HOST, SERVER_PORT, self._application)