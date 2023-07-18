This project was built for one of our clients, Md. Kazi. We tried to develop this soluion as per client's requirement.

**Our initial homepage looks like this**
![](assets/intial%20homepage.png)

**Our initial admin panel looks like this**
![](assets/initial%20admin%20panel.png)
![](assets/initial%20admin%20panel%202.png)

<br><br>

### You will find some necessary instructions below
<details> 
<summary>How to create a django project</summary>

To install django and create a django project first open a folder and then move into that folder and open terminal do the following steps(in the terminal).

```
pip install django --upgrade
django-admin startproject store
cd store
python manage.py runserver
```

You can use any preferred name instead of `store` .

</details>

<details> 
<summary>How to create a django app</summary>

To install app after creating a project run the following command in the terminal.

```
python manage.py startapp shop
```

You can use any preferred name instead of `shop` .

</details>

<details> 
<summary>What to do after making migrations(Ex.models.py or admin.py)</summary>

Run the following commands in the terminal 

```
python manage.py makemigrations
python manage.py migrate
```
</details>
