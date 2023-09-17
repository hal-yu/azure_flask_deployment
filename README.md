# azure_flask_deployment
Get hands-on experience setting up a Flask application, integrate it with data processing via Pandas, and deploy the app on Azure App Service. You'll also practice documenting your process and using GitHub for project management.

# Step-By-Step Guide Creating a New Data
1. Copy codes from Wk 2 folder from Professor Williams
2. Go to Haley's Week 2 Homework for HHA 507 and copy the raw data from diabetes.csv
3. Create a new file called diabetes.html
4. Go to app.py and create a new route to diabetes
5. Go to base.html and add in the new button to add diabetes to the list
6. Edit diabetes.html by copying information from data.html and change the header of the cells to fit the diabetes dataset

# Deploy to Azure
1. On google shell, copy the link  to get the CLI, test that it is installed and login with it
2. Create new web app service using "az webapp up --resource-group <name> --name <app-name> --runtime <PYTHON: 3.9> --sku <B1>"

### Azure Domain:
haley-504-flask-azuredep.azurewebsites.net
