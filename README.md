# DevOPS-Project
Here we will develop out own DevOPS Project


This project is a python software that deploys as a web service that shares the status of a site called "Site_Checker"

First search feature code steps:

1 - import the relevant library
2 - create a function that recieves an random site URL input from a user
3 - create a function that checks status of the url
4 - prints the output

Infrastructure dependencies:

1 MGMT instance (with terraform ansible and docker) that will run:
(package as a terraform script)
1 - create 3 **free** instances - 2 app instances
2 - create 1 load balancer
3 - create SG that allows all traffic in, through http 80
    and llows secured traffic from MGMT instance, through ssh 22


Infrastructure configuration:

create ansible script for the following:
1 - install docker on the app servers
2 - start docker service
3 - #disable SElinux#
4 - pull and run dockerfile from dockerhub.



