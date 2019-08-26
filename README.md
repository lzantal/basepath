# basepath
Simple base path function to avoid hardcoding file path

Use it to create a root base path and call it in your code to return the full path
without repeating the parent folder and/or subfolders name.
Add more subfolders as needed or new root folder without over writing the original one.

## Usage:
```
from basepath import bpath
tp = bpath('www')
```

Call it with a file name
```
tp('index.html')
'www/index.html'
```

Filename and optional folder name
```
tp('index.html','view_error')
'www/view_error/index.html'
```

You can add as many subfolder as you want to
```
tp('index.html','view_error','subfolder2','subfolderN')
'www/view_error/subfolder2/subfolderN/index.html'
```

To get the current base path call the function without arguments
```
tp()
'www/'
```

You can add subfolders to base path without a file by passing in an empty string
```
tp('','subfolder','another')
'www/subfolder/another/'
```

Replace the root folder, it will not overwrite the original one
```
tp('index.html', root='secret')
'secret/index.html'
```

You can add subfolders as well
```
tp('index.html', 'subfolder', root='secret')
'secret/subfolder/index.html'
```
