How to run the WebApp
----------------------------------------
1.Download the git by using command git clone https://github.com/developerarunvgk/ExcelFilterDB-Task

2.Ensure that python3 and pip3 are installed

3.Go to the extracted folder in the Directory and install the requirements using command pip3 install  -r requirements.txt or use pip install  -r requirements.txt

4.Open the terminal in folder where git is downloaded(or use cd command to go to file path) and Start the API using python3 manage.py runserver

5.As you are using localhost , go to web-browser and test it using API
http://127.0.0.1:8000/home/
Then Please Truncate and Load Data from here.
Proceed with Validations

Refer Screenshot_Output for the Result outputs

DB used is sqllite.
It can be modifed to any of the common RDMS by changing the settings in settings.py of Django.
