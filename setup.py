#!/usr/bin/env python

from setuptools import setup, find_packages, Extension

VERSION = (0, 0, 1)
VERSION_STR = ".".join([str(x) for x in VERSION])

setup(
    name='lz4ex',
    version=VERSION_STR,
    description="Comprehensive LZ4 Bindings for Python",
    license='BSD',
    long_description=open('README.md', 'r').read(),
    author='Jerry Ryle',
    author_email='jerryryle@gmail.com',
    url='https://github.com/jerryryle/python-lz4ex',
    packages=['lz4ex'],
    ext_modules=[
        Extension('lz4ex.lz4',
                  sources = [
                      'src/lz4/lz4.c',
                      'src/python-lz4.c'],
                  define_macros = [
                      ('LZ4_VERSION', '"%s"' % 'r131'),
                      ('VERSION', '"%s"' % VERSION_STR)],
                  extra_compile_args=[
                      "-std=c99",
                      "-O3",
                      "-Wall",
                      "-W",
                      "-Wundef"]
                  ),
        Extension('lz4ex.lz4hc',
                  sources = [
                      'src/lz4/lz4hc.c',
                      'src/python-lz4hc.c'],
                  define_macros = [
                      ('LZ4_VERSION', '"%s"' % 'r131'),
                      ('VERSION', '"%s"' % VERSION_STR)],
                  extra_compile_args=[
                      "-std=c99",
                      "-O3",
                      "-Wall",
                      "-W",
                      "-Wundef"]
                  ),
        Extension('lz4ex.lz4frame',
                  sources = [
                      'src/lz4/lz4.c',
                      'src/lz4/lz4frame.c',
                      'src/lz4/lz4hc.c',
                      'src/lz4/xxhash.c',
                      'src/python-lz4frame.c'],
                  define_macros = [
                      ('LZ4_VERSION', '"%s"' % 'r131'),
                      ('VERSION', '"%s"' % VERSION_STR)],
                  extra_compile_args=[
                      "-std=c99",
                      "-O3",
                      "-Wall",
                      "-W",
                      "-Wundef"]
                  )
    ],
    setup_requires=["nose>=1.0"],
    test_suite="nose.collector",
    keywords=['lz4ex', 'lz4', 'lz4hc', 'lz4frame'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
