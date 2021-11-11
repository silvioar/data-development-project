# Crypto data in Power BI dashboard which updates every hour

The project got a python script which creates a table with some crypto data. This script is hosted in a EC2 AWS Instance that runs every hour at minute 20. The table created with the python script goes to MySQL automatically and then this SQL table goes to a Power BI dashboard. 
So, the Power BI Dashboard updates every hour with some crypto data.

![image](https://user-images.githubusercontent.com/71708004/141308527-feb64805-15bc-4dfc-a26b-09f16855bcfd.png)

## EC2 INSTANCE
I created a EC2 instance in AWS:
 

Once the instance was created I deal with the .PEM and the .ppk files to activate the virtual machine.
When I complete those steps, I finally could run it via Putty:

![image](https://user-images.githubusercontent.com/71708004/141308579-a68f0db3-865e-44d8-965d-e6b136b11885.png)

 
Once these steps were completed I created a virtual environment, installed git and clone the actual github repository.
After that, I checked the python version and then I installed the librarys required, with the requieriments.txt file.

Also I created a crontab file which contains the log of the python file. This crontab file allows to schedule the running of the script and also it creates a txt file with the prints of the script. 
In my case, my crontab is 
20 */1 * * * cd /home/ec2-user/project/project && /home/ec2-user/project/python_env/bin/python /home/ec2-user/project/project/project_github.py  >>/home/ec2-user/project/project/cron_project.txt 2>&1

It says that the script will run every hour at minute 20 and also it will create a txt file with the log (cron_project.txt)
So if I open this txt file it will contain something like this

![image](https://user-images.githubusercontent.com/71708004/141308600-428a9f71-5a2b-40e0-8306-35c5eba03d44.png)
 

## Python script
It is a simple script which got data from Coingecko API, showing the price, market cap and volume of some criptos.
After that, the final table will be sent to MySQL automatically and will replace all the values of the table from the DB
After that, this updated table every 1 hour goes to a Power BI dashboard and the process will repeat every hour at minute 20.

## Power BI Dashboard
Power BI got some limitations if you want to publish on their APP, allowing to do this only for the PRO users. In my case, I’m not a PRO user so I could publish the dashboard but it can’t be updated automatically because the programmed update is not available.
Here is the link to the dashboard (you'll need an account):
https://app.powerbi.com/groups/me/reports/d1e356d3-0233-44e8-8942-c3c7af03e671?ctid=4c818f79-ab84-4552-9b7c-2fe715b0d0d5&pbi_source=linkShare

And here is a screenshot of the (simple) dashboard.

![image](https://user-images.githubusercontent.com/71708004/141308635-c58908b9-5c43-4cac-a875-d67e63da211a.png)


