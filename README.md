#Odoo 10 Development Essentials
This is the code repository for [Odoo 10 Development Essentials](https://www.packtpub.com/big-data-and-business-intelligence/odoo-10-development-essentials?utm_source=github&utm_medium=repository&utm_campaign=9781785884887), published by [Packt](www.packtpub.com). It contains all the supporting project files necessary to work through the book from start to finish.
## About the Book
Odoo is one of the fastest growing open source, business application development software products available. With announcement of Odoo 10, there are many new features added to Odoo and the face of business applications developed with Odoo has changed. This book will not only teach you how to build and customize business applications with Odoo, but it also covers all the new features that Odoo has to offer.
##Instructions and Navigations
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter02.



The code will look like the following:
```
@api.multi
def do_toggle_done(self):
for task in self:
task.is_done = not task.is_done
return True
```

We will install our Odoo server on an Ubuntu or Debian system, but we expect you to use your operation system and programming tools of choice, be it Windows, Mac, or other. We will provide some guidance on setting up a virtual machine with Ubuntu Server. You should choose a virtualization software to use, such as VirtualBox or VMWare Player; both are available for free. If you are using a Ubuntu or Debian workstation, no virtual machine will be needed. As you already figured, our Odoo installation will be using Linux, so we will inevitably use the command line. However you should be able to follow the instructions given even if not familiar with it. Basic knowledge of the Python programming language is expected. If you're not comfortable with it, we advise you to follow a quick tutorial to get you started. We will also make use of XML, so it is desirable to be familiar with the markup syntax.

##Related Products
* [Odoo Development Cookbook](https://www.packtpub.com/big-data-and-business-intelligence/odoo-development-cookbook?utm_source=github&utm_medium=repository&utm_campaign=9781785883644)

* [Working with Odoo](https://www.packtpub.com/big-data-and-business-intelligence/working-odoo?utm_source=github&utm_medium=repository&utm_campaign=9781784394554)

* [Odoo Development Essentials](https://www.packtpub.com/big-data-and-business-intelligence/odoo-development-essentials?utm_source=github&utm_medium=repository&utm_campaign=9781784392796)
###Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSe5qwunkGf6PUvzPirPDtuy1Du5Rlzew23UBp2S-P3wB-GcwQ/viewform) if you have any feedback or suggestions.
