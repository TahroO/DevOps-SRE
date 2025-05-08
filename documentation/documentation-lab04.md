# Documentation

## B21.1 - B23.1 WTAT2: DevOps and Site Reliability Engineering (SL) - 1. Zug - WiSe2024/25

*Bernd Reusch* - s0587188

### Lab 04-containerization

- [sharedRepo](/assets/dockerHubShared.png)


Initial thoughts and assumptions:

> Until the exercise, I only knew docker from theory. But I found the topic very exciting. 
> Due to my experience with Flask, I had already installed docker on my computer shortly before the exercise. 
> Since I use Linux, I worked completely via the CLI.

Describe the process of solving the tasks:

> I found it very helpful that we went through this together during the exercise. Basically, the container worked, 
> but it was a bit complicated for me to find out how I had to define the ports so that something was displayed in 
> the browser. Hamzeh then pointed out to me that my Dockerfile was missing a 0 in the definition of the IP 
> address (I only had 3). Once this was fixed, everything ran smoothly.
> Another realization was that under Linux you always need sudo to execute docker commands.
> Pushing the image to Docker Hub was a bit complicated because I had to read up on it first and reset my password 
> because the one I chose during registration didn't work via CLI (special characters ^). 
> After the change I was able to log in and push the image accordingly. 
> This image could be found on [dockerHub](https://hub.docker.com/repository/docker/berndhtw/foobar/general).


Describe the final outcome:

> The executable image is now on the DockerHub and is split as required. I used the collaborators option for this, 
> similar to GitHub. In general, I found this exercise super helpful to get an understanding of Docker and will 
> hopefully be able to use these skills more often now.


