import pathlib

filenames =pathlib.Path()
for file in filenames.glob('*.py'):
    print(file)