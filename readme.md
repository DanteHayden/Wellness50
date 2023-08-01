# WELLNESS50
#### Video Demo:  <URL HERE>
#### Description:
Wellness50 is a web application built wiht flask in python language, the web app is a simple task manager with tasks suggestions to add and complete as you go on about your day, a daily quote tab and a diary for you to register any information about your day that you deem necessary. The app has a log in and register feature that were repurposed from the finance PSET, and the UI has a friendly aesthetic in mind as to make the user as comfortable as possible.


### How to run
To run this project you will need python, pip and flask installed, for python just follow through with this download link: https://www.python.org/downloads/ for the latest version, usually pip is automatically installed with the latest vesrion of Python, so no need to worries about that, on a command prompt type "pip install flask" and you should be set to download Wellness50 files to your computer, from the main folder of the project type "flask run", this should create a local instance of the website in your computer, and that's it!

### Files and functions
### app.py
app.py is the center of the program, with all the important functions that make a the web application open in the first place, most of the magic is done with flask that enables my python code to process and send in back to the HTML information. Down bellow i'm going to be listing some of the most interesting functions and others elements of my code that might be of interest.


### register()
register is responsible for taking information from register.html, checking if all forms where properly filled, giving out instructions using apology() in case the user misses out some important information and if all is done properly the function call the DB wellness.db in the users table and INSERT all the information of the user there, and giving him a unique userId property, that will be used to call his session and pull out all related information


### taskMaker()
The name is pretty much self explanatory, the function pulls out the createTask form from taskManager.html and inserts said info into the Tasks table on wellness DB to latter be pulled into taskManager


### taskManager.html
taskManager.html is the heart of the entire app, it is where all off the CRUD operations related to tasks are done, create, visualize, complete, delete and reset, all of them in one html page, that was the biggest achivement i was able to pull with this project, i was not aware that i could do multiple forms in one page, i though there were limitations in place with flask, but i was happily proved wrong about that. 


### taskSuggestions
I also would like to cite that insteat of creating a entire function only for suggestions i decided to just make it so that every task that userId 2 has is shown as a suggestion for every other user, shaving off some time that enabled me to work on other parts of the project.


### diary()
Diary is a simple form that you can store texts on, it displays on the same html page


### daily()
daily() picks a random quote from a table in wellness.db and presents it the user, it takes a different quote every time it reloads


### UI 
I used the finance PSET as a skeleton for the project and from there i started making changes to it until it had another aspect to it, Wellness50 has a navbar and other elements without any opacity and the background has a spinning circle with a soft green to blue gradient as to make it look less stale.



### FINAL CONSIDERATIONS
This was a project done single handledy by Daniel Stumm with the resources provided in CS50, CS50 was one of the most important courses i've taken in my career, the base knowledge i got from here helped me grow in ways i never imagined, i feel full of inspiration to take on greater challenges and i'm exited to start working on newer and more audacious projects. Thank you all!


