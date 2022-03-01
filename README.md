# Ptools library (Python tools library)
## Bundle of python wrappers

![](img/pytools.png)

this a bundle of libraries usefull to develop script to automate tasks

#### Dependencies
- pytest
- pytest-html
- unittest

#### set the environment to launch executable or test
> source the following file:
```
 source set_env.sh 

```
#### Run tests
> run the following command line:
```
 pytest tests

```
>remark: in the current context. tests is the name the directory that contains all the different tests
#### Run tests and generate html report
> run the following command line:
```
 pytest -v tests --html=tests_report.html --self-contained-html

```
> remark: the html report will be generated in the directory of execution
