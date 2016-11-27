#Odoo 10 Development Essentials - Second Edition
This is the code repository for [Odoo 10 Development Essentials - Second Edition](https://www.packtpub.com/big-data-and-business-intelligence/odoo-10-development-essentials-second-edition?utm_source=github&utm_medium=repository&utm_campaign=9781785884887), published by [Packt](www.packtpub.com). It contains all the supporting project files necessary to work through the book from start to finish.
## About the Book
Daniel Reis has worked in the IT industry for over 15 years, most of it for a multinational consultancy firm, implementing business applications for a variety of sectors, including telco, banking, and industry. He has been working with Odoo (formerly OpenERP) since 2010, is an active contributor to the Odoo Community Association projects, and has been a regular speaker at the OpenDays annual conference.
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

We will install our Odoo server on an Ubuntu or Debian system, but we expect you to use your operation system and programming tools of choice, be it Windows, Mac, or other. We will provide some guidance on setting up a virtual machine with Ubuntu Server. You should choose a virtualization software to use, such as VirtualBox or VMWare Player; both are available for free. If you are using a Ubuntu or Debian workstation, no virtual machine
will be needed. As you already figured, our Odoo installation will be using Linux, so we will inevitably use the command line. However you should be able to follow the instructions given even if not familiar with it. Basic knowledge of the Python programming language is expected. If you're not comfortable with it, we advise you to follow a quick tutorial to get you started. We will also make use of XML, so it is desirable to be familiar with the markup syntax.

##Related Products
* [Odoo Development Essentials](Current URL?utm_source=github&utm_medium=repository&utm_campaign=9781784392796)

* [Odoo Development Cookbook](https://www.packtpub.com/big-data-and-business-intelligence/odoo-development-cookbook?utm_source=github&utm_medium=repository&utm_campaign=9781785883644)

* [Working with Odoo](https://www.packtpub.com/big-data-and-business-intelligence/working-odoo?utm_source=github&utm_medium=repository&utm_campaign=9781784394554)
###Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSe5qwunkGf6PUvzPirPDtuy1Du5Rlzew23UBp2S-P3wB-GcwQ/viewform) if you have any feedback or suggestions.
