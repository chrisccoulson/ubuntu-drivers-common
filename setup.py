#!/usr/bin/env python

from distutils.core import setup

import subprocess, glob, os.path
import os

#mo_files = []
## HACK: make sure that the mo files are generated and up-to-date
#subprocess.call(["make", "-C", "po", "build-mo"])
#for filepath in glob.glob("po/mo/*/LC_MESSAGES/*.mo"):
#    lang = filepath[len("po/mo/"):]
#    targetpath = os.path.dirname(os.path.join("share/locale",lang))
#    mo_files.append((targetpath, [filepath]))

# Make the nvidia-installer hooks executable
for x in glob.glob("nvidia-installer-hooks/*"):
    os.chmod(x, 0755)

setup(
    name="nvidia-common",
    author="Alberto Milone",
    author_email="albertomilone@alice.it",
    maintainer="Alberto Milone",
    maintainer_email="albertomilone@alice.it",
    url="http://www.albertomilone.com",
    license="gpl",
    description="Find obsolete NVIDIA drivers",
    packages=["NvidiaDetector"],
    data_files=[("/etc/kernel/header_postinst.d/", glob.glob("nvidia-common")),
                ("/etc/kernel/postinst.d/", glob.glob("nvidia-common")),
                ("/usr/share/nvidia-common/", glob.glob("share/obsolete")),
                ("/usr/lib/nvidia/", glob.glob("nvidia-installer-hooks/*")),
               ],# + mo_files,
    scripts=["nvidia-detector"],
)