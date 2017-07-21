from conans import ConanFile, CMake, tools
import os


class GlewConan(ConanFile):
    name = "GLEW"
    version = "2.0.0"
    license = "MIT"
    url = "https://github.com/DarkMorford/conan-glew"
    description = "The OpenGL Extension Wrangler Library (GLEW) is a cross-platform open-source C/C++ extension loading library."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        tools.download("https://downloads.sourceforge.net/project/glew/glew/2.0.0/glew-2.0.0.tgz", "glew-2.0.0.tgz")
        tools.check_sha1("glew-2.0.0.tgz", "6e15c84f7e1fad34cd3679f784a233744ddf048f")
        tools.unzip("glew-2.0.0.tgz")
        os.remove("glew-2.0.0.tgz")

    def build(self):
        cmake = CMake(self)
        self.run('cmake hello %s' % cmake.command_line)
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]
