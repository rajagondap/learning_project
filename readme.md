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