# Documentation

## B21.1 - B23.1 WTAT2: DevOps and Site Reliability Engineering (SL) - 1. Zug - WiSe2024/25

*Bernd Reusch* - s0587188

### Lab 6-Docker-compose

- [clicksCollection](/assets/clicksCollection.png)

- [final result](/assets/timestampsHtml.png)  



Initial thoughts and assumptions:

> I was a bit scared about this lab first. The explanation from the assignment was not really clear to me when I was reading
> it before the lab. It was really great that we were going through the steps together during the lab-time, so I had a base
> to start from when working on it at home. It was also great that we had the opportunity to take a picture from the provided
> code from Stephan. I forgot to check out a new branch during lab, so I had to revert all made changes first to start
> from scratch again.

Describe the process of solving the tasks:

> I started with checking out a new branch and created the docker-compose.yaml with the code out of the lab. I missed out
> the app part with the last 3 variables for the MONGODB_PORT - USERNAME - PASSWORD but luckily Vivian provided my some help here.
> I also had a typing error on the first line so my db was not showing up when running docker-compose build and up afterward.
> After fixing this it still was not showing up - I started to rework the app.py file as I assumed that I need to make a click to
> generate a Timestamp and store it into the database to actually initialize the database with the first timestamp.
> I implemented the code according to the picture of the code from the lab. I had to import the pymongo package to use the MongoClient class.
> After running the code again with build and up commands my app was not starting - only the 2 database containers were showing up.
> Problem: An old Flask Version in the requirements.txt led to an error that the app was not building when running
> docker-compose build. As I do not use the Docker Desktop App I used docker ps to list all running containers.
> After 45 min trial and error going through the code 10 times searching for typing errors and a call with Vivian I found the error in the terminal 
> *ImportError: cannot import name 'url_quote' from 'werkzeug.urls' (/usr/local/lib/python3.8/site-packages/werkzeug/urls.py)*
> I pasted the error in google and found a possible solution on stackoverflow that I need to specify "Werkzeug=2.2.2" inside the requirements 
> [source](https://stackoverflow.com/questions/77213053/why-did-flask-start-failing-with-importerror-cannot-import-name-url-quote-fr)
> After fixing this my app was starting as intended. Following that I had to adapt the code so that the timestamps were
> not saved into my earlier timestamps array but into the database. The mongodb documentation helped my here how to insert
> the data when the POST event occurs using [collection.insertOne()](https://www.mongodb.com/docs/manual/reference/method/db.collection.insertOne/)
> which also creates the collection if there is no existing one. Objects are stored as JSON objects inside the database which
> were defined inside the parameters. After running this I was able to see the timestamps inside my database with the help of the browser-
> I also removed my timestamps array variable and the call to insert elements in it.
> For the GET Part I first searched the documentation to find a method which fits me needs. I found 
> [collection.find()](https://www.mongodb.com/docs/manual/reference/method/db.collection.find/) but I was not sure how
> to return a list of all objects. After some time I asked ChatGPT how to handle this, and it returned the hint of using
> the list command before the query. It also provided me the syntax for the doc for doc in timestamps iteration.
> Lastly I only needed to change the variable inside my JavaScript code using the new clicks data instead of the timestamps array.


Describe the final outcome:

> I am very happy that I was able to solve this lab accordingly. It was really satisfying seeing the timestamps inside the 
> database and the returned list inside the textfield. I think this lab was the hardest one until now and I felt a bit lost
> several times during solving this but seeing the result is also the most satisfying as well.
> The final application sets up the 2 database containers, starts the app container, generates timestamps when clicking
> the click! button, stores them into the database collection as JSON objects and retrieve those when using the update! button
> showing each timestamp out of the collection on a new line. 
> I learned a lot during the lab. The bug hunt was a challenge and learning how mongodb handles data as JSON objects was also
> very interesting as I only knew relational databases with table structures like MySQL until this point.
> Again it was also great working together with Vivian on that assignment which helped alot spotting bugs.



