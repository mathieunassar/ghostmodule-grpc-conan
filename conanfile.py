from conans import ConanFile, CMake, tools


class GhostmoduleConan(ConanFile):
    name = "ghostmodule-grpc"
    version = "1.0"
    license = "Apache License 2.0"
    author = "Mathieu Nassar mathieu.nassar@gmail.com"
    url = "https://github.com/mathieunassar/ghostmodule-grpc"
    description = "ghostmodule extension to integrate gRPC."
    topics = ("framework", "microservice", "command-line", "database", "grpc")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"

    requires = (
        "grpc/1.25.0@inexorgame/stable",
        "ghostmodule/1.4@mathieunassar/stable",
        "gtest/1.8.1@bincrafters/stable"
    )

    def source(self):
        git = tools.Git(folder="ghostmodule-grpc")
        git.clone("https://github.com/mathieunassar/ghostmodule-grpc.git", "master")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="ghostmodule-grpc", args=["-DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=TRUE"])
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses")
        self.copy('*', dst='include', src='ghostmodule-grpc/include')
        self.copy("*.lib", dst="lib", src="", keep_path=False)
        self.copy("*.a", dst="lib", src="", keep_path=False)
        self.copy("*", dst="bin", src="bin")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)

    def package_info(self):
        if self.settings.build_type == "Debug":
            self.cpp_info.libs = ["ghost_connection_grpcd"]
        else:
            self.cpp_info.libs = ["ghost_connection_grpc"]
