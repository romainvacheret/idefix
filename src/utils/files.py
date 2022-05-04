from os.path import join, abspath
from typing import NewType, Union

Path = NewType('Path', str)

def convert_to_absolute_path(path: Union[Path, list[str]]) -> Path:
	if isinstance(path, list) and len(path) > 0 and \
		all(isinstance(p, str) for p in path):
		path = join(*path)
	return abspath(path)
