Speed calculator
================

Program require the time and the distance to calculate the speed
----------------------------------------------------------------

You should enter the distance then the time the program will calculate the speed 
the current program will ask you to enter the speed then the distance once you type enter he will display the speed 
to run this program you should type:

.. code:: bash
python {file name}


These are the necessary step to do my test 
------------------------------------------
 
First we have to run our virtual machine if you don't have one create it using 
-sudo apt-get install vagrant 
to turn it on:

.. code:: bash
vagrant up 
vagrant ssh

Then we have to moove to venv using these commands:

.. code:: bash
pew ls (to list the exesited environements)
pew workon (name of the environement you like to workon) 


Installing python requirements 
------------------------------

Developement dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~ 
To install the dependencies we should run :

.. code:: bash
pip install -r requirements_dev.txt 

To check syntax error
--------------------
We are going to use pylint: 

.. code:: bash
pylint [name of the file that contain your code]

Pylint will display the syntax errors in your code and will indicate the concerned lines



To execute the code
-------------------
Using pytest:

.. code:: bash
pytest [name of the file that contain the code]
