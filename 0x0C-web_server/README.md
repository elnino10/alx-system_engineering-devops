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

### Resources
Several resources are provided to aid in understanding and completing the project. These include information on how the web works, Nginx configuration, child process concepts, DNS, HTTP requests, and more.
- [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
- [How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)
- [Root and sub domain](https://landingi.com/help/domains-vs-subdomains/)
- [HTTP redirection](https://moz.com/learn/seo/redirection)
- [Not found HTTP response code](https://en.wikipedia.org/wiki/HTTP_404)
- [Logs files on Linux](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)

### References
- [RFC 7231 (HTTP/1.1)](https://datatracker.ietf.org/doc/html/rfc7231)
- [RFC 7540 (HTTP/2)](https://datatracker.ietf.org/doc/html/rfc7540)

### man or help
- scp
- curl

## Learning Objectives
Upon completing this project, you should be able to explain the following without relying on Google:

- The main role of a web server.
- What a child process is.
- Why web servers have parent and child processes.
- Main HTTP requests.
- DNS and its main role.
- DNS Record Types: A, CNAME, TXT, MX.

## Requirements
The project has specific requirements, including the choice of editors to use (vi, vim, or emacs), interpreting files on Ubuntu 16.04 LTS, newline endings, a mandatory README.md file, executable Bash scripts, passing Shellcheck without errors, and specific comments in the Bash scripts.

Servers
The project involves configuring and managing a web server.
