# Configuration Management README

## Overview
This project Introduces the concept of `configuration management` with focus on `puppet` as a configuration management tool. There are other tools which include `Ansible`, `Saltstack`, `Chef`, etc. but for this project, our focus is on puppet. These tools are also called `Automation tools`. They are used to make the management and configuration of servers and resources more reliable and faster.

## Background Context
When I was working for SlideShare, I worked on an auto-remediation tool called Skynet that monitored, scaled and fixed Cloud infrastructure. I was using a parallel job-execution system called MCollective that allowed me to execute commands to one or multiple servers at the same time. I could apply an action to a selected set of servers by applying a filter such as the server’s hostname or any other metadata we had (server type, server environment…). At some point, a bug was present in my code that sent nil to the filter method.

There were 2 pieces of bad news:

When MCollective receives nil as an argument for its filter method, it takes this to mean ‘all servers’
The action I sent was to terminate the selected servers
I started the parallel job-execution and after some time, I realized that it was taking longer than expected. Looking at logs I realized that I was shutting down SlideShare’s entire document conversion environment. Actually, 75% of all our conversion infrastructure servers had been shut down, resulting in users not able to convert their PDFs, powerpoints, and videos… Pretty bad!

Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1H, pretty impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways)…

Obviously writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.

#### Credit: Sylvain Kalache

## Requirements
### General
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension .pp

##  Install `puppet`
```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```

## Install `puppet-lint`
```
$ gem install puppet-lint
```

## Resources
- [Intro to Configuration Management](https://intranet.alxswe.com/rltoken/GL30hu-aRcKzPOvK8JO-Bg)
- [Puppet resource type: file](https://intranet.alxswe.com/rltoken/WON0M4DNRabf88KAG_pDUA)
- [Puppet’s Declarative Language: Modeling Instead of Scripting](https://intranet.alxswe.com/rltoken/0V2fBdafkfKPMxA1umea3Q)
- [Puppet lint](https://intranet.alxswe.com/rltoken/CRUMeEMdcX-UtbWsUM9xLQ)
- [Puppet emacs mode](https://intranet.alxswe.com/rltoken/MzHXCntAkPzOqMnI6_rpWQ)

### Example Task
```
Using Puppet, create a file in /tmp.
Requirements:
  File path is /tmp/school
  File permission is 0744
  File owner is www-data
  File group is www-data
  File contains I love Puppet
```

### Solution
```
# Create a file in /tmp called school
file { '/tmp/school':
  path    => '/tmp/school',
  content => 'I love Puppet',
  owner   => www-data,
  group   => www-data,
  mode    => '0744',
}
```
