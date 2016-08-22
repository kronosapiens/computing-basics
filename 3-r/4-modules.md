# Modules

Modules in R work similary to modules in Python, and the same principles apply. You can import a module/package/library from the standard library, by downloading a third-party library, or by writing a module yourself.

## Import Syntax

```
library(<library_name>)

source("<your_file>.R")
```

For libraries, either in the standard library or third-party, are imported using the `library` function. For code you've written yourself, you call the `source` function on the file containing that code. In both cases, all the functions inside these modules are imported.

Note that to import code you've written yourself, you must pass the file name including either a full or relative path to the current directory that R is running in.


## Third-Party Libraries

To install a third-party library, you use the `install.package` function, passing the name of the library as a string:

```
install.package("<library_name>")
```