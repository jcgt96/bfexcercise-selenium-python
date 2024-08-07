
# Selenium with python

Based on the Gherklin lenguaje, here is a framework using Behave that is the equivalent of Serenity BDD in Python. Here is used the POM (Page Object Model Pattern).

# Installing Dependences

Its recommended to work under a virtual enviroment. For that, the first is to create one.

Creating a virtual enviroment: 

```
python3 -m venv venv
```
Once created, the following step is to rise the enviroment.

Windosws:
```
venv\Scripts\activate
```

MacOs and Linux:

```
source venv/bin/activate
```

You will know that the env is already risen when in your terminal starts with (venv).

Now, in your virtual enviroment you need to install the dependences that are required to run this project. For that, run the following command:

```
pip install -r requirements.txt
```

verify the installation:

```
pip list
```

Now you are set to work and run! 

To run all the scernarios described in the .feature file just run the following command:

```
behave
```
