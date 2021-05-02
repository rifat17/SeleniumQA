# Selenium Page Object Model with Python 

Page-object-model (POM) is a pattern that you can apply it to develop efficient automation framework. With page-model, it is possible to minimise maintenance cost. Basically page-object means that your every page is inherited from a base class which includes basic functionalities for every pages.


## Project Overview

#### at first clone the repo
```sh
git clone https://github.com/rifat17/SeleniumQA.git

cd SeleniumQA
```

#### install dependancies

```shell
python -m venv venv
source ./venv/bin/activate
pip install -r requirments.txt
```


#### If you want to run all tests, you should type: 
```sh
python -m unittest QUP01.tests.bk.all_tests 
```


#### If you want to run just a class, you should type: 
```sh
python -m unittest QUP01.tests.bk.test_google_home_page
```

#### If you want to run just a test method, you should type: 
```sh
python -m unittest QUP01.tests.bk.test_google_home_page.GoogleHomepage.test_check_page_loaded
```