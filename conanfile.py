from conans import ConanFile, tools
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake
import os.path


class Hello(ConanFile):
    name = "hello"

    settings = {
        "os": ["Windows"],
        "compiler": None,
        "build_type": None,
        "arch": None
    }
    options = {"shared": [True, False]}
    default_options = {
        "shared": True
    }
    
    generators = "CMakeDeps"
    exports_sources = "*"
    no_copy_source = True

    def build_requirements(self):
        self.build_requires("cmake/3.17.1")

    def layout(self):
        self.cpp.package.includedirs = ["include"]
        self.cpp.package.libs = ["hello"]

    def generate(self):
        tc = CMakeToolchain(self, generator="Ninja")
        version = tools.Version(self.version)
        tc.variables["VERSION"] = version
        tc.variables["PROJECT_VERSION"] = version
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        
    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()
