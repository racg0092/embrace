# EMBRACE
`Embrace` is a CLI (Command Line Interface) tool that provides assistance and automation for software developers. The goal is to provide complex scaffolding for projects so that repetetive tasks and snippets of codes are automatically done or generated for you.

## Installation
In the future we plan to publish this as a [npm](https://www.npmjs.com/) package so it will be easy to downlad and install. There are also plans to implement [npx](https://www.npmjs.com/package/npx) to have the user run builds and scripts without the need to isntal the binaries locally.

As of now you will need to clone this repo and build the package yourself if you want to use `Embrace`.

`Prerequisites`
- [Python3](https://www.python.org/)
- [PIP](https://pypi.org/project/pip/)
- [pyinstaller](https://www.pyinstaller.org/)

`Embrace` is a build using python3 so you will need [Python3](https://www.python.org/) if you want to run the script locally without having to build the binaries. First verify that you have python installed in your system if you don't refer to the website to download and install.

`How to verify?`

### windows 10
Open `powershell` or `cmd(command pormpt)` and run the following command to check if python is in your system.

```sh
 > python --version
```
`output`: Python 3.9.1+

If you don't get the above command go to the website, download and install [Python3](https://www.python.org/).

### Linux
If your working in Linux `python` is usually already install. However to make sure that is run the following command to check.

```sh
$ python3 --version
```
`output`: Python 3.9.1+

If you don't get the about output run the following command.

```sh
$ sudo apt install python3
```
`note`: Depending on your Linux destribution you may need to use a different package manager.

### PIP
PIP is usually installed when python3 is installed. In case it is not you can refer to the [pip](https://pypi.org/project/pip/) website and download it manually.