from setuptools import setup, find_packages

setup(
    name='hand_controller',
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
    entry_point={
        'console_scripts': [
            'hand_controller = hand_controller.main:run'
        ]
    },
)