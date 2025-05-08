# Documentation

## B21.1 - B23.1 WTAT2: DevOps and Site Reliability Engineering (SL) - 1. Zug - WiSe2024/25

*Bernd Reusch* - s0587188

### Lab 02-service-creation

Initial thoughts and assumptions:

> During the lab I was a bit overwhelmed by the flask installing process. As there were so many different
> operating systems it was a bit tricky to follow the workflow which was shown to create the application.
> I also had some issues with adding the flask .bin to my PATH variable first.
> At the end of the lab I managed to run flask but accidental I had 2 instances of Pycharm running with 2
> applications. Because of that my changes to the code were not reflected in the browser.
> I also managed to implement the index.html and copied the code stump for the
> GET and POST request functions. During the following days I solved most of my earlier problems.

Describe the process of solving the tasks:

> I started to research different sources about flask itself. With this I was able to correctly respond with
> my index.html file if the root directory is requested. I decided that I want to start with the GET Request
> first and tried to find existing online solutions for that method. The problem for me here was what I should
> do with this 'clicks' rule parameter. I knew that it should react to the clicks of the html buttons and tried
> to find something that would help me to implement this via python in flask. After some time I realized, that
> somehow the GET must be sent from the Frontend and not the Backend. Now it became clearer for me, so I
> implemented some JS functions which should be called when the "onclick" event happens. I followed that trail
> and searched next how to make GET or POST request inside that functions and discovered fetch().
> By adding my 'clicks' to the parameters of fetch I now realized that this was my missing piece to connect
> Front- and Backend.
> With the help of my browser deftools I proofed my way in seeing that there were actually GET and POST
> request send after clicking the buttons. Later I thought about what to do on the Backend with those requests
> and decided to implement only one function and not 2 functions to handle the requests.
> The last step was to create and send a JSON with the UNIX Timestamp. For that I also had to look up how to get the
> unix time stamp and learned that unix time is not depending on the timezone. I stored those timestamp inside a
> global array variable. To actually get a json returned I looked up the jsonify method from python.
> During the process my app was reworked several times.

Describe the final outcome:

> The final app fulfills all tasks which were requested by the lab description. The web service is able to
> respond with the html and handles POST and GET requests. The Frontend is connected to the Backend and the buttons
> are working like intended. Using Post the JSON with the UNIX timestamp is returned. Using GET the timestamps are
> returned and shown in the textarea via the JavaScript inside the html by using the timestamps global variable.
> During this lab I learned a lot about Flask, the broader picture of Front- and Backend connection, how requests are
sent and refreshed my knowledge about UNIX time and Markdown.



Sources:

https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24  
https://www.geeksforgeeks.org/flask-http-method/  
https://www.geeksforgeeks.org/how-to-convert-datetime-to-unix-timestamp-in-python/  
https://stackoverflow.com/questions/16036041/can-a-html-button-perform-a-post-request  
https://www.youtube.com/watch?v=Up5Gm_Ls2oQ  
https://www.markdownguide.org/basic-syntax/  
https://chatgpt.com  
*(used for final unix timestamps showing in html textarea as I was not sure how to transfer the variable from flask)*
*(Prompt: Take the given code and explain how to show the unix timestamp from flask inside the textfield)*
