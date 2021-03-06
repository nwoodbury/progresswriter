#!/usr/bin/env python

from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys
import os


class PyTest(TestCommand):
    def finalize_options(self):
        os.system('printf "\033c"')
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='progresswriter',
    version='0.0.1',
    packages=['progresswriter'],
    scripts=[],
    include_package_data=True,
    install_requires=[],
    tests_require=[
    ],
    cmdclass={'test': PyTest},
)
