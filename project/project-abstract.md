# Project Abstract - IMI Project CMS monitoring with Grafana and Prometheus

## Project description

This project looks at how Prometheus and Grafana can be used to monitor a web server application,  
using the example of our project Drupal CMS. 
Prometheus collects data about server performance, such as resource usage, response times, and errors.  
Grafana helps by turning this data into clear, easy-to-read dashboards and graphs and is able to set up alerts  
under certain conditions. 

### Context

One part of our IMI Project is a Content Management System which uses Drupal and Maria DB. This stores and handles  
all media files and our points of interest object data which is at some point exported as json to be used  
inside a HoloLens2 Application generating AR Layouts from its content.  
At the moment our Drupal CMS has no metrics which are available to make sure that everything works like we want.  
Actually there is only the native Drupal application running on a virtual linux server in the hetzner environment.


### Purpose

I want to monitor our Drupal CMS which is used in our IMI Project. The Goal is to observe the stability and availability  
of the resources used, to measure the traffic which goes in and out, the available space and that the database works healthy.  
This should improve the insights and reliability of our overall project.

### Method

*needed resources*

All needed resources should be available through research on the internet. As both applications are open source  
there should be no problem to get them running. There are plenty of available predefined dashboard which could be  
adapted to my needs. The server on hetzner is owned privately and therefore should be accessible and maintainable  
during the project timeframe.

*overall timetable*

- week 1 - research on prometheus, needed dependencies, installation on the virtual server, configuration and get it running

- week 2 - research on grafana, needed dependencies, installation on the virtual server, configuration and get it running

- week 3 - research on dashboards, and the query language needed for information retrieval from prometheus

- week 4 - refinement and first version implementation of a working dashboard

- week 5 - final refinement and preparation of project presentation

*risks*

The only risk I see is that I do not get prometheus running on the server in the given timeframe and therefor would  
not be able to retrieve the needed data for grafana. There is also the risk that the provided data is not enough  
to show something "excited" but I assume the way should be the goal here!

### Expected Results

At minimum one working grafana dashboard showing several data information regarding the server status and used resources, traffic  
of users and available space using prometheus as datasource.