# DevOps & Site Reliability Engineering

### This repository represents my entire lab and project work for the course DevOps and Site Reliability Engineering, which I attended in the winter semester 2024/25.

LabWork Topics include:  
> - create a **Flask** service and handle GET and POST requests for a small click application
> - solve all **git branching** puzzles from [learngitbranching](https://learngitbranching.js.org/)
>   - - [Main](/assets/03-git-branching-main.png)
>   - - [Remote](/assets/03-git-branching-remote.png)
> - protect the main branch inside a GitHub Repository from pushing without a **pull request**
> - create a **Docker Image** and push it to Docker hub
> - create a **GitHub Actions Pipeline** and use it to push the **Docker Image** automatically when merging branches into main
>   - - [final pipeline](/assets/failedPipelineDocker.png)
> - create a **MongoDB Database**, store timestamps from the **Flask App** in it and run all together inside a **Docker container**
>   - - [clicksCollection](/assets/clicksCollection.png)
>   - - [final result](/assets/timestampsHtml.png) 
> - research different ways and providers to run **kubernetes** either locally, self-managed or fully managed in the cloud
> - create a local **minikube kubernetes environment** and run the **Flask App** container in it
>   - - [final result app](/assets/workingTimestamps.png)
> - use **Terraform** and **Infrastructure as Code** to create a GitHub Repository with a provider and the HashiCorp Configuration Language (HCL)


The Final Project:



> The project aimed to create a **Grafana dashboard** to monitor server status, resource usage, traffic, and storage  
> using **Prometheus** as the data source. After setting up a second virtual server on Hetzner for data collection,  
> **Prometheus Node Exporter** was installed on the monitored server, and **Prometheus** was set up on the monitoring server.  
> **Grafana** was then installed and configured to display scraped data. Dashboards were built by customizing templates  
> from the **Grafana library**, adjusting panel queries, and refreshing the design.
>
> Additional features included configuring **alerts that trigger a Slack bot** when a server goes offline and  
> creating a **Grafana playlist** to cycle through dashboards every two minutes.  
> These features enhance usability and allow for efficient monitoring in office environments.  
> The primary goal of achieving a fully functional monitoring dashboard was successfully met.
> - [Final Dashboard Part 1](/assets/dashBoardFinal1.png)
> - [Final Dashboard Part 2](/assets/dashBoardFinal2.png)
> - [Grafana Dashboard JSON](/project/holoDahsboard.json)