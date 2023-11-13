# setup.py
from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
<<<<<<< HEAD
    install_requires=[],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz_script:main',
=======
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:main',
>>>>>>> 2a9b05835a11842f4c5245c8495f027001738ce6
        ],
    },
)
