## Load balancer README

## Overview
In this project, we delve into two fundamental concepts that play crucial roles in the world of web development: Load Balancing and Web Stack Debugging. Understanding these concepts is essential for building scalable and reliable web applications.

### Load Balancer:
The importance of load balancing, a technique that distributes incoming network traffic across multiple servers to ensure optimal resource utilization, minimize response time (ensures low latency), and prevent overload on any single server. The implementation of how to configure web servers and load balancers to achieve high availability and fault tolerance in web applications.

![load_balancer](https://github.com/elnino10/alx-system_engineering-devops/assets/103988900/61ec0176-588c-4632-b930-d9fefa9e5b5d)
### Web Stack Debugging:
Mastering the art of debugging in a web stack environment or as a software engineer is an essenial skill to have in one's toolbox, though it comes with the wealth experience an individual has in a field. The experience help to uncover the common challenges developers face while identifying and fixing issues within the intricate layers of a web application.

#### Test and verify your assumptions
The idea is to ask a set of questions until you find the issue. For example, if you installed a web server and it isn’t serving a page when browsing the IP, here are some questions you can ask yourself to start debugging:

- Is the web server started? - You can check using the service manager, also double check by checking process list.
- On what port should it listen? - Check your web server configuration
- Is it actually listening on this port? - netstat -lpdn - run as root or sudo so that you can see the process for each listening port
- It is listening on the correct server IP? - netstat is also your friend here
- Is there a firewall enabled?
- Have you looked at logs? - usually in /var/log and tail -f is your friend
- Can I connect to the HTTP port from the location I am browsing from? - curl is your friend
There is a good chance that at this point you will already have found part of the issue.

#### Get a quick overview of the machine state
This concept introduces the first five(5) commands to use when starting out your exammination

`w`
- shows server uptime which is the time during which the server has been continuously running
- shows which users are connected to the server
- load average will give you a good sense of the server health - (read more about load here and here)

`history`
- shows which commands were previously run by the user you are currently connected to
- you can learn a lot about what type of work was previously performed on the machine, and what could have gone wrong with it
- where you might want to start your debugging work

`top`
- shows what is currently running on this server
- order results by CPU, memory utilization and catch the ones that are resource intensive

`df`
- shows disk utilization

`netstat`
- what port and IP your server is listening on
- what processes are using sockets
- try netstat -lpn on a Ubuntu machine

## Background Context
You have been given 2 additional servers:

- `gc-[STUDENT_ID]-web-02-XXXXXXXXXX`
- `gc-[STUDENT_ID]-lb-01-XXXXXXXXXX`
Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

## Resources

- [Introduction to load-balancing and HAproxy](https://intranet.alxswe.com/rltoken/B7f3oz8i3Xvvom_YQZzLnQ)
- [HTTP header](https://intranet.alxswe.com/rltoken/sZ9v3Vq2tgLwN_PWVQketw)
- [Debian/Ubuntu HAProxy packages](https://intranet.alxswe.com/rltoken/2VRAgtKKR9g6Xfb0xzGiSg)

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on `Ubuntu 16.04 LTS`
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `Shellcheck (version 0.3.7)` without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks
`Task 0 Double the number of web servers`

In this first task you need to configure web-02 to be identical to web-01. Fortunately, you built a Bash script during your web server project, and they’ll now come in handy to easily configure web-02. Remember, always try to automate your work!

Since we’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.

Requirements:

  - Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
    - The name of the custom HTTP header must be X-Served-By
    - The value of the custom HTTP header must be the hostname of the server Nginx is running on
  - Write 0-custom_http_response_header so that it configures a brand new Ubuntu machine to the requirements asked in this task
    - Ignore SC2154 for shellcheck
   
### Example
```
elnino10@ubuntu$ curl -sI 34.198.248.145 | grep X-Served-By
X-Served-By: 03-web-01
elnino10@ubuntu$ curl -sI 54.89.38.100 | grep X-Served-By
X-Served-By: 03-web-02
elnino10@ubuntu$
```
