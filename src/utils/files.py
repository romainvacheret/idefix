from os import listdir
from re import search
from os.path import join, abspath
from typing import NewType, Union

Path = NewType('Path', str)


def convert_to_absolute_path(path: Union[Path, list[str]]) -> Path:
	if isinstance(path, list) and len(path) > 0 and \
		all(isinstance(p, str) for p in path):
		path = join(*path)
	return abspath(path)


def _select_variants_folders(folder: Path) -> list[str]:
	is_variant = lambda folder: search('^variant-[0-9]+$', folder)
	return list(filter(is_variant, listdir(folder)))


def _read_file(path: Path) -> str:
	with open(path, 'r') as file:
		return file.read()


def list_generated_variants(folder: Path) -> list[dict]:
	variants = _select_variants_folders(folder)
	return [{'id': variant, 'diff': _read_file(join(folder, variant, 'patch.diff'))} \
		for variant in variants]