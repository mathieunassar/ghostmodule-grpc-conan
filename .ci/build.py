from cpt.packager import ConanMultiPackager
import os

if __name__ == "__main__":
    project_remotes = ["https://api.bintray.com/conan/mathieunassar/ghostrobotics", "https://api.bintray.com/conan/bincrafters/public-conan", "https://api.bintray.com/conan/inexorgame/inexor-conan"]
    remotes = os.getenv("CONAN_REMOTES", project_remotes)
    builder = ConanMultiPackager(upload_dependencies="all", build_policy="missing", remotes=remotes)
    builder.add_common_builds(shared_option_name="ghostmodule-grpc:shared")
    builder.run()
