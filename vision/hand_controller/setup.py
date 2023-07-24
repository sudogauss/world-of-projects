from setuptools import setup, find_packages

setup(
    name='handcontroller',
    version='1.1.0',
    description='A python script/service which helps to control screen actions with hands',
    author='sudogauss',
    author_email='t.liashkevich1772@gmail.com',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'mediapipe',
        'pyautogui',
        'pyyaml'
    ],
    entry_points={
        'console_scripts': [
            'hand-controller = handcontroller.main:run'
        ]
    },
)