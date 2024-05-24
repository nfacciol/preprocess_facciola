import setuptools

with open('README.md', 'r') as file:
	long_description = file.read()


setuptools.setup(
	name = 'preprocess_facciola',
	version = '0.0.1',
	author = 'Nicholas Facciola',
	author_email = 'nicholas.facciola@intel.com',
	description = 'This is a preprocessing package',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Python :: 3',
	'License :: OSI Approved :: MIT License',
	"Operating System :: OS Independent"],
	python_requires = '>=3.5'
	)