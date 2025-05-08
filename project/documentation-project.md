# Documentation

## B21.1 - B23.1 WTAT2: DevOps and Site Reliability Engineering (SL) - 1. Zug - WiSe2024/25

*Bernd Reusch* - s0587188

### project - prometheus and grafana Holo-CMS

Screenshots 

- [Final Dashboard Part 1](/assets/dashBoardFinal1.png)
- [Final Dashboard Part 2](/assets/dashBoardFinal2.png)

TLDR - Summary:

> The project aimed to create a Grafana dashboard to monitor server status, resource usage, traffic, and storage  
> using Prometheus as the data source. After setting up a second virtual server on Hetzner for data collection,  
> Prometheus Node Exporter was installed on the monitored server, and Prometheus was set up on the monitoring server.  
> Grafana was then installed and configured to display scraped data. Dashboards were built by customizing templates  
> from the Grafana library, adjusting panel queries, and refreshing the design.  
>   
> Additional features included configuring alerts that trigger a Slack bot when a server goes offline and  
> creating a Grafana playlist to cycle through dashboards every two minutes.  
> These features enhance usability and allow for efficient monitoring in office environments.  
> The primary goal of achieving a fully functional monitoring dashboard was successfully met.
>
> 
Initial thoughts and assumptions:

> I had a clear plan how to approach this project. Following my project abstract there was a defined goal already.  
> First I was a bit unsure about how I would handle configuring  
> prometheus and receive the scraped data inside grafana but during the initial research phase I was able to  
> find a lot of information about the needed steps to make this working.
> 
> I also planned to include some extra features if I would have enough time:  
>   
> - Grafana Alerts - Define some alters on a metric which should be triggered in case  
> - Slackbot - A bot which handles information flow defined inside grafana, posting alerts in a Slack-Channel  
> - Playlist - use the grafana playlist option to show at least 2 different dashboards on a screen  
> 

Describe the process of solving the tasks:

> What was done before: initial actions
> 
> Hetzner Server - setUp second box
> 
> Due to the fact I chose the way of implementing Prometheus with the scheme of one observed and a collecting server,  
> I had to set up a second virtual box on the Hetzner server for collecting data from the node exporter and using  
> grafana in a later stage to display those data. This was done with a little help from my boyfriend using ansible as I  
> was not that firm with the handling of ansible and setting up virtual boxes. The ansible yaml file acts like Terraform  
> we used during the exercises, where I could describe the desired state of the box and ansible will handle to run the commands.  
> Inside the file I described variables like:  
>   
> 
> - desired IP Address and name of the server
> - ssh key to connect with
> - the jump-host which to be used for the connection
> - the user creation
>   
> The ssh config which was used to connect to the server via terminal later on used my usual public keyfile. This  
> is stored inside a hidden folder called ./ssh/config. It is some kind of textfile containing following information:  
> (values omitted due to security reasons)  
>   
> - web-bernd-h1
> - Host web-bernd-h1
> - HostName  
> - UserPrerequisites  
> - ProxyJump  
> - IdentityFile

> After the setup progress was done I had a base to start with installing the tools I would need:  
> I was following a tutorial on the hetzner documentation setting up prometheus on the monitored server and monitoring server.  
>  
>       - monitored node - 10.10.1.42 - CMS node
> 
> First I had to install the [Prometheus Node exporter](https://github.com/prometheus/node_exporter) which listens on HTTP port 9100 on the server which  
> should be monitored to scrape the observation-data. As root User on the Server I had to run a Terminal, followed by  
> setting up a connection via ssh. To verify the outcome I used the curl command  
> which proofed the working exporter. During the process I had to install curl first -
> 
> - [MonitoredServerPrometheus](/assets/curlMonitored.png)  
>    
> 
>       - monitoring node - 10.10.1.43 - prom node
> 
> To actually collect the data from the earlier configured node exporter I had to set up an additional prometheus server.  
> The earlier created second box was used on that. As this was a new node I had to install apt and update it first to  
> later install prometheus. 
> Next a prometheus.yaml was needed to describe the target which to scrape from. This was done via Terminal -   
> I used vim to adjust the content later on and added a scrape configuration like showed at the Hetzner Site.  
> 
> - [MonitoringServerPrometheus](/assets/prometheusServer.png)
> 
> I restarted the Prometheus service used curl again which returned that the service was running like intended.  
> 
>       - install grafana
> 
> The last step of qwq installation process was to enable the grafana repository, install grafana on the prometheus  
> server and enable/start the daemon. To reach the webinterface and import prometheus as a data-source I had to use ssh  
> port forwarding to make the server reachable from the outside. After doing so I used the webinterface and configured it  
> to make the scraped data available on my dashboards from prometheus.
> 
>       - first dashboard and building process
> 
> I already had some knowledge about building dashboard from my working student job last semester. Usually I start by  
> searching the [Grafana Dashboard Library](https://grafana.com/grafana/dashboards/) for suitable pattern dashboards  
> which provide parts of a possible solution. I started with 3 different prometheus server dashboards and inspected  
> their panel elements and configuration. Afterward I copied a dashboard and started to delete unneeded panels and  
> added panels from the other dashboards. During this process I am able to customize the appearance and the data I      
> want to observe. Some panels needed to be adjusted in regards their queries as they are either scraping wrong metrics  
> or are somehow misconfigured for my needs. Mostly I had to change the instance and job variable as my dashboard had  
> different data variables defined.  
> Please also see my [Grafana Dashboard JSON](holoDahsboard.json), which could be imported by other users to adapt  
> my design and configuration. Due to the fact, that there might be different variables defined the user may add some  
> changes to the queries to get this working.
>  
>   
>       - used commands for installation and configuration
>   
>   - monitored node
> 
> apt update
> apt install prometheus-node-exporter
> 
>   - monitoring node
> 
> apt update
> apt install prometheus jq
> 
>   - install grafana
>
> apt install apt-transport-https software-properties-common wget
> wget -q -O - https://packages.grafana.com/gpg.key | apt-key add -
> echo "deb https://apt.grafana.com stable main" > /etc/apt/sources.list.d/grafana.list  
> 
> apt update
> apt install grafana
> systemctl enable grafana-server.service
> systemctl start grafana-server.service
> 
>   - ssh port forwarding 
> 
> ssh -L 3000:10.10.1.43:3000 -N -f jumphost-h1

Describe the final outcome:

> - The goal for this project was defined as:  
> *At minimum one working grafana dashboard showing several data information regarding   
> the server status and used resources, traffic of users and available space using prometheus as datasource.*
> 
> This is reached. I have a working dashboard monitoring the 4 golden Signals as mentioned during the lecture.  
> These are shown on top of this documentation screenshots.
> 
>       - Additional Outcome:
> 
> Custom Dashboard Configuration
> 
> - A custom dashboard was created using a standard dashboard as a base. All Panels removed and structure rebuilt  
> including panels from other dashboards and complete self-made panels. The whole design was also refreshed and updated.
> 
> Alert-Configuration and Slack Alert Bot
> 
> - I was additionally able to set up an alarm if the server status switches to offline. A configured Slack Bot will  
> trigger and post this alert into a defined Slack channel. This could be useful for the escalation process.  
> The Slack Bot was created following the [Grafana SlackBot Guide](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/manage-contact-points/integrations/configure-slack/)
> 
> Grafana Playlist option
> 
> - A Playlist was created, switching between 2 Monitoring Boards in a timeframe of 2 minutes. This would be useful  
> if the monitoring should be shown on a tv screen inside an office.
> 
> 
> 
> 

Sources:

> https://community.hetzner.com/tutorials/install-and-configure-prometheus-stack



