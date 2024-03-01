import os
import shutil

for base, folders, files in os.walk('/Users/malkoch/Documents/GitHub/ToG-Builder/ToG-Builder/Packages'):
    for file in files:
        if '.dll' in file and 'netstandard2.0' in os.path.join(base, file):
            print(os.path.join(base, file))
            shutil.copy(os.path.join(base, file), file)
