# 0x0C Web Server Project README

### Project Overview
This project, titled "0x0C. Web server," is centered around DevOps and SysAdmin. It entails the installation and configuration of a web server as a hands on learning by practice

## Objectives
The primary objectives of this project is understanding "What a Child Process is" with exercises on configuring the web-01 server according to specified requirements and automating tasks using Bash scripts.

## Example Script
An example script is provided to illustrate how to automate tasks. The key is to avoid manual intervention and script the configurations.

```bash
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
```

# Resources
Several resources are provided to aid in understanding and completing the project. These include information on how the web works, Nginx configuration, child process concepts, DNS, HTTP requests, and more.

# Learning Objectives
Upon completing this project, you should be able to explain the following without relying on Google:

- The main role of a web server.
- What a child process is.
- Why web servers have parent and child processes.
- Main HTTP requests.
- DNS and its main role.
- DNS Record Types: A, CNAME, TXT, MX.

# Requirements
The project has specific requirements, including the choice of editors, interpreting files on Ubuntu 16.04 LTS, newline endings, a mandatory README.md file, executable Bash scripts, passing Shellcheck without errors, and specific comments in the Bash scripts.

Servers
The project involves configuring and managing a web server.
