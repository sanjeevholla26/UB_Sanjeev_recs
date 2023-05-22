# UB_Sanjeev_recs
<br>

#### This is a project done for the recruitment of Uthkrusht Web team. I have choosen the 1st task i.e Career Development Module. Here is the detailed report of this project.
<br>

### Video Recording of the project.
https://drive.google.com/drive/folders/1joObjl0EglddnW8IwlZSwfoG0lSvK3y1?usp=share_link
<br>

### Installation instructions to set up the project from scratch :

1. To run this project you need to install ***Django*** as this project is made by django framework.
   In the command promt or terminal give the following command 
   <br>
   
         pip install django
      
   <br>
2. After the installation has completed, you can verify your Django installation by executing the following command in the    command prompt or terminal.
   <br>
   
         django-admin --version
      
   <br>


### Steps to run the project :
1. Once you install django then either you have to clone this repository or you need to fork it. If you want to clone this repository then run the command following command in the terminal or command promt
   <br>

         git clone https://github.com/sanjeevholla26/UB_Sanjeev_recs.git

   <br>

2. After cloning the repository change the directory to the project directory. For that give the command 
   <br>
   
         cd IRIS_Rec23_221IT059_Django/sangam
      
   <br>
   
3. In order to apply all the migrations to the database run the following two commands
   <br>

         python3 manage.py makemigrations
   
   <br>
  
         python3 manage.py migrate
   
   <br>
   
   [***NOTE*** : If the version of python in your pc is 3 then only give python3 int the command or else just give python.]
   <br>
   
4. In order to start the project run the command 
   <br>

          python3 manage.py runserver
    
   <br>
5. After you run the command then go to any web browser and go to the url ***"http://127.0.0.1:8000/"*** to see the website. 

<br>

   ### Features Implemented in the project 
   

1. ***User Registration and login*** : In this web application only the authorized users can use it. So a user need to register himself to use this account. If he had an account already then he wants to login with that account.
2. ***Using sessions*** : Sessions have been used in order to keep the user loged in to the application. So there is no need for the user to again and again login to the website each times he visit it.
3. ***Viewing the discussion rooms*** : Once a User is loged in, he will be able to see all the discussion rooms available and can see the details of the discussion rooms.
4. ***Posting your Ideas*** : User can see all the conversations happened in a particular discussion room and even he can post his ideas on that discussion room.

### Planned features :
<br>

1. I want to improve the front end of the website.
2. Addind the notification feature so that the user will be notified on the activities going on in the platform.
3. Search functionality.
4. Creating profile.
5. Editing of the discussion room by its owner.
<br>

### References used :
<br>

1. Google is the main source of reference.
2. For frontend I have used ***Bootstrap***.

