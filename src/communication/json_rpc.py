from __future__ import annotations
from typing import NoReturn, Final

from src.communication.server_wrapper import ServerWrapper
from src.utils.files import convert_to_absolute_path

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from jsonrpc import JSONRPCResponseManager, dispatcher

SERVER_HOST: Final = '127.0.0.1'
SERVER_PORT: Final = 8080


def compile_program(engine, path, command) -> bool:
	path = convert_to_absolute_path([engine.PROJECTS_FOLDER, path])
	return engine.compile_program(path, command)


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

	def serve(self) -> NoReturn:
		run_simple(SERVER_HOST, SERVER_PORT, self._application)