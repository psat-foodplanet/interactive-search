from setuptools import find_packages, setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='interactive-search',
    version='0.0.1',
    ## requierement 설치
    packages=find_packages(),
    ## 명령어로 사용하게끔
    ## terminal 명령어 = 폴더.파일:함수
    entry_points={
        "console_scripts": [
            "ship-cli = shipcommand.cli:cli"
        ]
    },
    ## 이하의 폴더에서 경로에서 import
    py_modules=["src"],
    ## 이하 안 중요
    url='https://github.com/psat-foodplanet/interactive-search',
    license='MIT',
    author='PSAT',
    author_email='natasma13@gmail.com.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    # install_requires=required,
    description='Interactive Search Project'
)
