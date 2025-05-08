# Documentation

## B21.1 - B23.1 WTAT2: DevOps and Site Reliability Engineering (SL) - 1. Zug - WiSe2024/25

*Bernd Reusch* - s0587188

### Lab 9-terraform


Initial thoughts and assumptions:

> The concept of infrastructure as code was new to me. Learning that we just need to describe in code what kind of  
> infrastructure we want to create and just hand this over to terraform sounds like a great way to manage resources in  
> a cloud or data center. [Terraform-Website](https://www.terraform.io/)

Describe the process of solving the tasks:

> During the lab I first followed Stephan creating a server in the Hetzner Cloud with Terraform. As I did not have  
> a paid Hetzner Cloud subscription I choose another way to solve this lab by creating a GitHub repository via terraform.  
> I installed Terraform for Ubuntu following the given commands from the [installation-side](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)  
> To know what I have to do next I searched in the [Terraform-Registry](https://registry.terraform.io/providers/integrations/github/latest/docs) for the gitHub provider.
> First 3 essential files were created.  
> 
> - main.tf - defining the resources to be created in the target cloud
> - provider.tf - contain the terraform block, configurations and aliases
> - terraform.tf - holds the required provider information - in my case I had to use the > version 0.13 option  
> 
> Next I choose the authentication method handled in the provider file. I created a gitHub Token with the help of the  
> [gitHub webinterface](https://github.com/settings/tokens) only providing repo access and rights which was put into a  
> .gitHubTokenFile inside the terraform folder, marked invisible. I also added this file to the .gitIgnore file to don't  
> leak my token to anyone. I need to use the (classic) token version from gitHub here. Inside the provider.tf I now assign  
> this token to a variable using trimspace (removing whitespaces) providing the path to the file.  
> Later on I had to remove the provider from the main.tf as it was copied falsy from my side in there.  
> After defining the tf files accordingly I executed terraform init and terraform plan and received an error first. After  
> changing the path to my gitHub token file to the correct one it ran as expected. Finally, I typed terraform apply to  
> adapt all settings from the plan command and actually create my gitHub Repo and it worked. Destroy should remove the  
> repo after execution, but after I did not provide the rights to delete repos during the key generation the repo still exists.
> 
> 
> 

Describe the final outcome:

> I am very happy with the outcome and that I managed to solve this during lab time - I never heard about a way to  
> create gitHub repos outside gitHub or the commandline and was impressed how well this works. With my implementation  
> Iam now able to create repos automated if I want to.
> 
> commands to remember:
> - terraform init - initialize terraform  
> - terraform plan - tell me what should be done to be set up  
> - terraform apply - execute the plan
> - terraform destroy - destroys the actual running infrastructure  
> 
> [source1](https://spacelift.io/blog/terraform-files)  
> [source2](https://medium.com/@tony.infisical/guide-to-using-oauth-2-0-to-access-github-api-818383862591)




