import os
from glob import glob
from setuptools import setup

package_name = 'tform'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shriram',
    maintainer_email='dshriram27@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
             "circ=tform.circ:main",
             "dyn=tform.dyn:main",
             "dyn2=tform.dyn2:main",
        ],
    },
)
