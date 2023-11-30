### Creating simple Django project




### Creating Super User

django at main site - is a user-friendly application to administrate the contents of a relational database
linked to a Django project.

One of the most powerful parts of django is the automatic admin interface

It takes Matadata from your models to provide quick, model centric interface where trusted users can manage content 
on your site.



### View Function

It is a python file which receives and web request and returns a web response.

Two types: 
1. Function based view
2. Class based view

We will study about function based views

### Django models

Building blocks for the django projects.

The typical way for Django applications to interact with data is using Django models. Django model
is an object-oriented Python class that represents the characteristics of an entity.

A model is the single, definitive source of information about your data. 
It contains the essential fields and behaviors of the data you’re storing. 
Generally, each model maps to a single database table.

A model is the single, definitive source of information about your data. 
It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

**The basics:**

Each model is a Python class that subclasses django.db.models.Model.
Each attribute of the model represents a database field.
With all of this, Django gives you an automatically-generated database-access API


### Django model relationship

**1. Many-to-One Relationship**

**2. One-to-One Relationship**

**3. Many-to-Many Relationship**


### Register a Django model

### Django Templates
For rendering templates in django we use render function. It combines the given template with the 
given dictionary, and returns http response with returned text. you can pass different arguments in render function.
some of them and required and some are optional.

**Required arguments**

**request** The Request object is used to generate the response.

**template_name** The full name of a template to use or sequence of template names.

**Optional Arguments**

**context** A dictionary of values to add to the template context. By default, this is an empty dictionary. 
IF value in the dictionary is callable, the view will call it just before rendering the template.

**content_type** The MIME type to use the resulting document. Default to 'text/html'.

**status** The status code for the response. Default to 200.

#### Template inheritance

#### Adding CSS and Bootstrap Style

#### Creating Dynamic Slug with signals

django includes signal dispatcher which helps decoupled applications get notified when action occurs elsewhere in the framework
and an actual signal that allows certain senders to notify a set of receivers
that some action has taken place.

They're especially useful when many piece of code may be interested in the same events.


**Note - We will write more about Signals and slug here**


#### Django - Retriving Data




