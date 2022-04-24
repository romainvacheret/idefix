from os import getcwd
from os.path import join

from src.tools.astor_engine import AstorEngine

if __name__ == '__main__':
	engine = AstorEngine()
	project_path = 'projects/Math-issue-280'
	project_full_path = join(getcwd(), project_path)
	parameters = {'-mode':  'jgenprog',
		'-srcjavafolder': '/src/java/',
		'-srctestfolder': '/src/test/',
		'-binjavafolder': '/target/classes/',
		'-bintestfolder':  '/target/test-classes/',
		'-location': project_full_path,
		'-dependencies': f'{project_full_path}/lib'}
	successfully_compiled = engine.compile_program(project_full_path)

	if successfully_compiled:
		successfully_ran = engine.run(parameters)