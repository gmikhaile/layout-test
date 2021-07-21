cls

set CONAN_VERBOSE_TRACEBACK=1

conan create . ^
hello/0.1.0@atd/testing ^
--profile "x86_64-Windows-v142-Debug"
