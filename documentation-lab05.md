# Documentation

## B21.1 - B23.1 WTAT2: DevOps and Site Reliability Engineering (SL) - 1. Zug - WiSe2024/25

*Bernd Reusch* - s0587188

### Lab 5-gitHub actions

- [sharedRepo](/assets/dockerHubShared.png)
- [dockerHub Link](https://hub.docker.com/repository/docker/berndhtw/foobar/general)
- [final pipeline](/assets/failedPipelineDocker.png)  



Initial thoughts and assumptions:

> Due to the fact that I was working in presence at my working student job
> in Graz Austria this week I was not able to attend the lecture on monday.
> Luckily Vivian and Sarah provided me their notes about this topic afterward.
> I am already aware of automated testing pipelines in GitLab as we are using them
> at work when pushing new branches with created code before a merge request is created.
> Until this week I did not know that GitHub provides such a tool as well.

Describe the process of solving the tasks:

> I was researching the GitHub Actions Documentation in preparation to this week's lab.
> The actual process of creating the workflows directory and the .yaml file was straight forward.
> Vivian provided me some help about what code needed to be inside and how to create the GitHub Secrets.
> Again I messed up the password and username part like I did last week so my first attempt
> failed. I think I need some kind of password manager here as the amount of passwords and accounts
> is increasing week by week...
> After providing the correct password I restarted the pipeline with the help of the
> GitHub online interface. The next error occurred due to a missing $ sign before
> GITHUB_SHA but this was spotted relatively quick and was fixed directly.


Describe the final outcome:

> After providing the correct password and fixing the missing $ sign everything worked like expected.
> I was happy to see that all stages went green and that the image was finally pushed to DockerHub afterward.
> Using GitHub Actions seems like a real great functionality I now want to use more often in my repositories.



