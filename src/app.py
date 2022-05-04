from threading import Thread

from src.tools.astor_engine import AstorEngine
from src.communication.server_wrapper import ServerWrapper
from src.communication.ftp import FTPServerWrapper
from src.communication.json_rpc import JsonRpcServerWrapper

class Application:
	def __init__(self) -> None:
		self._engine = AstorEngine()
		self._ftp_server = FTPServerWrapper()
		self._json_rpc_server = JsonRpcServerWrapper(self._engine)

		self._servers: list[ServerWrapper] = [self._ftp_server, self._json_rpc_server]
		self._threads: list[Thread] = []

	def launch_servers(self) -> None:
		for server in self._servers:
			self._threads.append(Thread(target=server.serve))
			self._threads[-1].start()