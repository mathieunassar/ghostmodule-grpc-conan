``` ascii
                                                   ____
_______  _      _  ______  ________ _________      '_' \
|  _____ |______| |      | |_______     |        \_\    \_/    _
|______| |      | |______| _______|     |           \____\____|_|
```

# Conan recipe for ghostmodule-grpc

ghostmodule (https://github.com/mathieunassar/ghostmodule) extension to integrate gRPC.

https://github.com/mathieunassar/ghostmodule-grpc

|     Build system     |                         Build status                         |
| :------------------: | :----------------------------------------------------------: |
|  Windows (Appveyor)  | [![Build status](https://ci.appveyor.com/api/projects/status/rfup183lv0v28b4n/branch/master?svg=true)](https://ci.appveyor.com/project/mathieunassar/ghostmodule-grpc-conan/branch/master) |
| Linux & OSX (Travis) | [![Build Status](https://travis-ci.com/mathieunassar/ghostmodule-grpc-conan.svg?branch=master)](https://travis-ci.com/mathieunassar/ghostmodule-grpc-conan) |

## Issues

If you wish to report an issue or make a request for a package, please do so here:

https://github.com/mathieunassar/ghostmodule/issues

## Usage

The Conan recipe to add to your setup is the following:

```
ghostmodule-grpc/1.0@mathieunassar/stable
```

#### Add Remote

The packages from this recipes are not located in the conan-center Bintray repository. You will need to add the following remote to your conan installation to locate the recipe:

```
$ conan remote add ghostrobotics "https://api.bintray.com/conan/mathieunassar/ghostrobotics"
```

## License Information

Bincrafters packages are hosted on [Bintray](https://bintray.com) and contain Open-Source software which is licensed by the software's maintainers and NOT Bincrafters.  For each Open-Source package published by Bincrafters, the packaging process obtains the required license files along with the original source files from the maintainer, and includes these license files in the generated Conan packages.

The contents of this GIT repository are completely separate from the software being packaged and therefore licensed separately.  The license for all files contained in this GIT repository are defined in the [LICENSE.md](LICENSE.md) file in this repository.  The licenses included with all Conan packages published by Bincrafters can be found in the Conan package directories in the following locations, relative to the Conan Cache root (`~/.conan` by default):

### License(s) for packaged software:

```
~/.conan/data/<pkg_name>/<pkg_version>/bincrafters/package/<random_package_id>/license/<LICENSE_FILES_HERE>
```

*Note :   The most common filenames for OSS licenses are `LICENSE` AND `COPYING` without file extensions.*

### License for Bincrafters recipe:

```
~/.conan/data/<pkg_name>/<pkg_version>/bincrafters/export/LICENSE.md
```
