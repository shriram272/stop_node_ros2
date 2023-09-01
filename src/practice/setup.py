from setuptools import setup

package_name = 'practice'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            "node1=practice.node1:main",
            "controller=practice.controller:main",
            "pose=practice.pose:main",
            "circ=practice.circ:main",
            "move2=practice.move2:main",
            "parabolic_curve=practice.parabolic_curve:main",
            "parabola=practice.parabola:main",
           
            

        ],
    },
)
