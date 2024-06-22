

# Extracting a zipfile to memory with Python
```python
from zipfile import ZipFile
from StringIO import StringIO

def extract_zip(input_zip):
    input_zip=ZipFile(input_zip)
    return {name: input_zip.read(name) for name in input_zip.namelist()}
```
#### References:
- https://stackoverflow.com/questions/10908877/extracting-a-zipfile-to-memory

