from zipfile import ZipFile
import os.path

zf_path = os.path.join('data', 'mechfiles', 'mechs.zip')

with ZipFile(zf_path) as mechzip:
    print(mechzip.namelist())
