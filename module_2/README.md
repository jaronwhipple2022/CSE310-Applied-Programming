# Overview

This was a fun little side project that I created to learn more about interacting with a data base through Python. I haven't
actually created the products that I uploaded to my data base, but I am working on designs and thought it could be useful some
day when I actually release my products. The idea behind it is that I could manage my product information through this app rather than directly editing it in the cloud.

[Software Demo Video](https://youtu.be/tbUAPiNNV28)

# Cloud Database

I created a free Google Firebase account and used it for my project.

The structure is very simple: I created three collections (a collection is a container for documents) that store similar items together. (hats, t-shirts, and sweat shirts.)

# Development Environment

I used Python in Visual Studio Code to complete this. I connected to my Fire Store using a service key (not included in my repository.) Modules to complete this included firebase_admin credentials and firebase_admin firestore.

# Useful Websites

- [Google Firebase](https://firebase.google.com/docs/firestore/data-model)
- [Youtube Playlist](https://www.youtube.com/playlist?list=PLs3IFJPw3G9LW-rGJ8EBMaCd8OxGm_qQe)

# Future Work

- When an item is updated, edited, or created, it is inserted as a dictionary. This causes the new information to appear as a dictionary and it stands out from the rest of the data. As an aesthetic appearance I would like to change it to be the same data-type and remove the brackets.

- Another improvement I would make is change the way data is displayed when you view it. It just shows up as a string dump and all the informationn is displayed without a particular order.

- Once my website is up and my products are listed I will connect this database to my website to help me keep track of stock and sales.
