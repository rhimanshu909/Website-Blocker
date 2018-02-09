# Website-Blocker

A Udemy Project

This is an app which will help you to block all the websites which you don't want to open or get open by itself. Also, blocking some social networking sites during your office/working hours. It will run in the background of your system and won't let you open the sites, which will hamper your productivity. It is very small in size so you don't have to worry about system performance and can be used in day-to-day life.

This app is developed using python. This is an app made while developing my existing python skills through Udemy course.

For Winodows
1.) Save program as .pyw extension instead of .py extension.
2.) Use Task Scheduler from search in start menu.
3.) Create New Task and check all the necessary configuartions.

For Linux/Mac
1.) Flush the cache through terminal just in case, not necessary though by dscacheutil -flushcache
2.) Set the host path to be "/etc/hosts"
3.) Use sudo crontab -e to add @reboot python path_of_program.py
  * You can alternatively use vim
  
Some websites have started using IPV6, so couldn't block by only IPV4 127:0:0:1. They have to be blocked on both IPV4 and IPV6 addresses fe80::1%lo0 or ::1. 
