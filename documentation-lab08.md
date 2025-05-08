# Documentation

## B21.1 - B23.1 WTAT2: DevOps and Site Reliability Engineering (SL) - 1. Zug - WiSe2024/25

*Bernd Reusch* - s0587188

### Lab 8-kubernetes-deployments

- [final result app](/assets/workingTimestamps.png)

Initial thoughts and assumptions:

> At the first look I was overwhelmed by the amount of information during the online lecture. The following first half of
> the exercise made things worse because there was a lot of new information to digest what was actually happening in k8s
> and what commands we would use to manage our yaml files and minikube.

Describe the process of solving the tasks:

> Luckily Stephan shared his .yaml files with us over GitHub so we could copy those, this helped a lot as we first had not 
> type those, making typos and indentation errors, and we had a lot more time to explore the commands and actually play around
> with our local k8s setUp. This made things so much more clear. One important thing to mention was that the image name inside
> the containers block of the deployment.yaml must match with the name on DockerHub including the Git-SHA Hash which we
> implemented earlier during the GitHub Actions exercise. It was also important to make sure that all yaml files are applied
> and that all services and pods are running. I had one issue relating to minikube -> after calling minikube tunnel
> I was not able to reach "localhost:5000" in my Browser because Minikube was tunneling to 10.104.72.27:5000 but with a little
> help I realized that. I was also using kubectl describe pod mongodb-0 to check if my database was running correct
> as my clicks were not showing. The [result in the terminal](/assets/imagePullBackoff.png) showed me that it took some time
> for the image to be pulled. I first looked up the imagePullBackOff Error I received and learned that there is an option
> to always look only locally for my database image by including imagePullPolicy: Never inside my deployment.yaml
> Due to the fact this worked without the addition after a short waiting time I will skip this change for now.  
> [Source](https://coding-stream-of-consciousness.com/2019/12/23/minikube-imagepullbackoff-local-docker-image/)

Describe the final outcome:

> After playing around with the working k8s environment, exploring more and more information and cool features I am 
> very impressed how cool it felt to set up this and watching it running. I learned a lot about k8s during the last 2 lectures
> and exercises and I would love to go deeper into that topic maybe related to my project idea working with grafana.
> 
> 
> commands to remember:
> - minikube start
> - minikube tunnel
> - minikube version
> - kubectl get pods
> - kubectl get service
> - kubetcl get replicasets
> - kubectl get deployments
> - kubectl describe pod [Name]
> - kubectl describe service [Name]
> - kubectl logs [Name]
> - kubectl apply -f [Path to file]
> - watch kubectl get pods -n kube-system



