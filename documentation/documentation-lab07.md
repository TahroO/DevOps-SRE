# Documentation

## B21.1 - B23.1 WTAT2: DevOps and Site Reliability Engineering (SL) - 1. Zug - WiSe2024/25

*Bernd Reusch* - s0587188

### Lab 7-Kubernetes-hosting



## Locally - [Kind](https://kind.sigs.k8s.io/)
> 
> kind is a tool for running local Kubernetes clusters using Docker container “nodes”.  
> kind was primarily designed for testing Kubernetes itself, but may be used for local development or CI.
> - benefits:
> 
> supports Linux, macOS and Windows - supports building Kubernetes release builds from source -  
> supports multi-node (including [High-availability-cluster](https://en.wikipedia.org/wiki/High-availability_cluster)) clusters -  
> open source - kind is a [Cloud-native-certified-kubernetes-installer](https://landscape.cncf.io/?selected=kind) - 
> full control over all aspects
> 
> - tradeoffs:
> 
> Container simulation lacks OS-level isolation, sharing the host’s kernel, which can complicate OS-specific testing
> scaling have to be done by ourselves -  
> relatively large image sizes - there are some known issues that might affect
> desired functionality [known-issues-list](https://kind.sigs.k8s.io/docs/user/known-issues/) - complexity has to be self-handled
> 
> - costs:
> 
> Due to the fact this is open source there is no cost for the software itself -  
> but keeping in mind the time I would have to invest and the required hardware to run and orchestrate the cluster   
> locally and also the investment in up and downscaling I consider it kind of expensive in a professional environment
> 
> - limitations, risks and security implications:
> 
> security has to be handled on my side - this may introduce several issues like permission problems, access issues and other
> [security-context-kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)
> 
> - creation and scaling:
> 
> Following the instructions kind may be installed from release binaries, source or package manager.
> Go provides inbuilt packages - As I am a Linux User I would use the Linux binary -
> [kind-releases](https://github.com/kubernetes-sigs/kind/releases)  
> 
> For AMD64 / x86_64  
> [ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.25.0/kind-linux-amd64  
> chmod +x ./kind  
> sudo mv ./kind /usr/local/bin/kind
> 
> Creation - use *kind create cluster* - This will bootstrap a Kubernetes cluster using a pre-built node image -  
> By default, the cluster will be given the name kind. Use the --name flag to assign the cluster a different context name -  
> 
> >Example:  
> >*kind create cluster* - default name kind  
> >*kind get clusters* - will list clusters  
> >*kubectl cluster-info --context kind-kind* - interaction  
> >*kind delete cluster* - deletes the cluster  
> more information see: [further-information-quick-start-guide](https://kind.sigs.k8s.io/docs/user/quick-start/)
> 
> scaling:  
> directly scaling when creating the cluster
> using [Terraform](https://www.terraform.io/) for automated scaling with 
> [horizontal-pod-autoscaler](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/horizontal_pod_autoscaler)
> 
> - recommendation:
> 
> kind offers a balanced compromise between compatibility and performance - open source seems attractive -  
> I would use it on a personal level or in a home environment for self-made projects
> 
> - sources: 
> [4-ways-to tun-kubernetes-locally](https://opensource.com/article/20/11/run-kubernetes-locally) - 
> [single-node-kubernetes-showdown](https://oilbeater.com/en/2024/02/22/minikube-vs-kind-vs-k3d/) -
> [how-to-scale-kind-cluster](https://stackoverflow.com/questions/69645357/how-to-scale-kind-cluster)

## Cloud provider - [DigitalOcean](https://www.digitalocean.com/products/kubernetes)
> 
> Powerful, cost-effective cloud infrastructure optimized for startups, growing digital businesses, and independent software vendors (ISVs)  
> DigitalOcean offers an easy-to-use managed Kubernetes service that provides fast deployment and integration with other DigitalOcean services
> - benefits:
> 
> easy scaling - without manual intervention  
> takes care of infrastructure and administrative tasks - highly available and fault-tolerant, 
> reducing the likelihood of service disruptions and ensuring the high availability of applications,  
> maintenance and updates are done by provider
> 
> - tradeoffs:
> Depending on IaaS, PaaS or fully managed  
> Iaas - droplets are totally self-managed – you choose what you put on them, and you manage any software on them yourself  
> PaaS - you lose some flexibility. It’s not totally portable, and the deployment configuration will be cloud provider specific  
> fully managed - still complex. DigitalOcean’s managed Kubernetes is as simple as possible, but simple Kubernetes still 
> require significant learning
> 
> overall downsides - data will be stored in a cloud service by a provider - no full control
> 
> - costs:
> 
> Different pricing models to choose from:
> > - Control Plane is free
> > - Droplet nodes - start at $12/month per node - free inbound data transfer - 2000GiB/month outbound free
> > - Block Storage - start at $10/month
> > - Load Balancers - start at $12/month per node
> > - Bandwidth - free, starting at 2,000GiB/node per month for Basic nodes
> > - Cilium Hubble-enhanced Kubernetes security and observability—at no additional cost
> 
> - limitations, risks and security implications:
> 
> limitations depends on pricing - for small businesses it may be too expensive to run 
> costs could be further increase if traffic goes up and up scaling is needed
> 
> - creation and scaling:
> 
> Create a DigitalOcean Account linked to a credit card  
> Create a project, and then from project page, click Manage -> Kubernetes (LTD)  
> Click Enable Limited Access and click Create a Kubernetes Cluster  
> Choose defaults - give it a name - optional add node pools - wait for build  
> setUp kubectl - config the kubeconfig file  
> confirm success using kubectl --kubeconfig=<PATH TO KUBECONFIG> get nodes
> 
> scaling - you can add additional nodes via the webinterface
> There is an [autoscaling-option](https://docs.digitalocean.com/products/kubernetes/how-to/autoscale/)
> 
> - recommendation:
> 
> could be an option for small scale startups depending on the chosen service type-
> If there are enough financial background this seems to be a good option to start into managed kubernetes hosting  
> Personally I would prefer this over AWS or Google Cloud as the starting price is much lower
> For large companies which may need more support and scaling or more flexible app integration AWS seems to be  
> more flexible but on a higher pricing tag
>
> - sources: 
> [comparing-10-managed-kubernetes-services](https://nordicapis.com/comparing-10-managed-kubernetes-services/) -
> [Kubernetes-on-DigitalOcean](https://geek-cookbook.funkypenguin.co.nz/kubernetes/cluster/digitalocean/)
> 
> 

## Self-managed - [vanilla-kubernetes](https://www.digitalocean.com/blog/vanilla-kubernetes-vs-managed-kubernetes)
>
> Unmanaged Kubernetes (also known as Vanilla or open source Kubernetes) refers to installing, deploying, and operating  
> Kubernetes yourself in your environment or on the infrastructure you control. With unmanaged Kubernetes, you handle  
> the end-to-end lifecycle which involves the process of installing, setting up the cluster, integrating adjacent systems,  
> managing the entire Kubernetes infrastructure, and keeping everything updated and running smoothly.  
> This offers more control but adds complexity.
> 
> - benefits:
> 
> complete control - possible to be used in on premise and multi-cloud environments - possible enhanced security -  
> possible savings on expenses if technical skills are existing and with good planning of resources
> 
> - tradeoffs:
> 
> Manual management of Kubernetes clusters can be complex and time-consuming - must allocate resources and personnel for  
> ongoing maintenance tasks - Unmanaged Kubernetes require careful planning and coordination to ensure optimal performance  
> and reliability - it is some kind of high responsibility for the team to keep things running
> 
> - costs:
> 
> the costs depend on the requirements, the technical knowledge, the load of traffic and data and existing hardware -  
> time costs must be considered to orchestrate the whole technical construct including maintenance and manpower
> 
> - limitations, risks and security implications:
> 
> If there are special security requirements which normally would not be considered with using a cloud provider  
> such as company constraints or data protection rules it could be better to implement those self - but you have  
> to know how to prevent security issues
> 
> The restrictions here depend on the hardware infrastructure, the knowledge of the platform engineers and the  
> time which it takes to do maintenance and keeping the things running. You always have to be on spot if anything  
> goes wrong to ensure reliability and stability of the system. 
> 
> - creation and scaling:
> 
> creation and requirements  [Tutorial-SetUp](https://medium.com/@ferdinandklr/creating-a-production-ready-self-hosted-kubernetes-cluster-from-scratch-on-a-vps-ipv6-compatible-660aa5018feb)
> 
> You need one or more machines running some Debian compatible Linux OS   
> 2GiB or more of RAM per machineI have 16GiB  
> At least 2 CPUs on the machine that is the Control-Plane  
> Network connectivity between nodes and each node must have a distinct MAC address and product_uuid  
> 
> > - create a new VPS node on cloud provider -> login on machine
> > - ssh setup - create root/.ssh/authorized_keys file & ssh public key - disable password authentication in
> > - upgrade packages: apt update && apt upgrade -y  
> > - possibly enable IPv6 
> > - validating IP addresses -> apt install iputils-ping -y & ping defined IPs
> > - Do IP Forwarding and Bridged Traffic
> > - Installing Container Runtime
> > - Enabling CRI API
> > - Enable Systemd CGroup Driver
> > - Installing Kubernetes Administrator
> > - Create new Dual Stack Cluster
> > - Accessing the Cluster using Kubectl
> > - Deploying a CNI
> > - Enabling Running Jobs
> > - Support for Load Balancing services
> > 
> 
> I found another exciting [Tutorial](https://developers.deepgram.com/docs/self-managed-kubernetes)
> 
> scaling
> 
> To scale things up we have to add other nodes to the cluster -  
> All nodes must be further orchestrated, registered and controlled / monitored
> 
> 
> - recommendation: 
>
> As it sounds exciting to manage my own kubernetes cluster the sheer amount of knowledge, installation and time  
> would be overwhelming. Considering using this in a professional environment needs a lot of manpower and money.
> This could be done for companies where resources do not matter or the need of security and data protection  
> is that high that it would be worth to invest in a self-managed infrastructure.
> 
> - sources: 
> 
> [5-important-facts-about-self-hosted-kubernetes](https://www.esono.de/blog/devops/self-managed-kubernetes-die-fuenf-wichtigsten-fakten_aid_1094.html) - 
> [unmanaged-vs-managed-kubernetes](https://www.digitalocean.com/resources/articles/unmanaged-vs-managed-kubernetes)

Describe the final outcome:

> The research part was a lot do but also very interesting. I am very proud of my outcome here.  
> The Minikube part was short and simple but also very rewarding seeing this running on my local machine.



