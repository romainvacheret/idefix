from os import getcwd, mkdir
from os.path import join, isdir
from typing import Final, NoReturn

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from src.communication.server_wrapper import ServerWrapper

SERVER_HOST: Final = '127.0.0.1'
SERVER_PORT: Final = 21
SERVER_USER: Final = 'idefix'
SERVER_PSWD: Final = 'idefix'
FOLDER_PATH: Final = 'projects'


class FTPServerWrapper(ServerWrapper):
	def __init__(self) -> None:
		self._authorizer = DummyAuthorizer()
		self._handler = FTPHandler
		self._handler.authorizer = self._authorizer
		self._server = FTPServer((SERVER_HOST, SERVER_PORT), self._handler)
		self._folder_full_path = join(getcwd(), FOLDER_PATH)

		self._create_folder()
		self._authorizer.add_user(SERVER_USER,
			SERVER_PSWD,
			self._folder_full_path,
			perm='elradfmwMT')

	def _create_folder(self) -> None:
		if not isdir(self._folder_full_path):
			mkdir(self._folder_full_path)

	def serve(self) -> NoReturn:
		self._server.serve_forever()