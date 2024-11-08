from Tools import tools_v000 as tools
from Jira import jira as j
from MyHours import myhours as m
import os
from os.path import dirname
import time
import tkinter as tk
from tkinter import messagebox


# False : If you have already start the clock => just update after. => Default value is True
isStartMyHoursNeeded = True

# -10 for the name of this project Start_Jira
# save_path = dirname(__file__)[ : -10]
save_path = os.path.dirname(os.path.abspath("__file__"))
propertiesFolder_path = save_path + "/"+ "Properties"

j.save_path = tools.readProperty(propertiesFolder_path, 'Start_Jira', 'save_path=')
j.jira = tools.readProperty(propertiesFolder_path, 'Start_Jira', 'jira=')

userJira = tools.readProperty(propertiesFolder_path, 'Start_Jira', 'userJira=')
passJira = tools.readProperty(propertiesFolder_path, 'Start_Jira', 'passJira=')

j.userInsim = tools.readProperty(propertiesFolder_path, 'Start_Jira', 'userInsim=')
j.userInsimPassword = tools.readProperty(propertiesFolder_path, 'Start_Jira', 'userInsimPassword=')

# Open Browser
tools.openBrowserChrome()

# MyHours part
m.connectToMyHours()
m.startTrack()


# Jira part
# j.loginToJira(userJira, passJira)
j.connectToJiraInsim(j.jira, j.userInsim, j.userInsimPassword)
# Need to wait if the browser ask for a user and password
# test if in the page we have the xpath of the button "//*[@id="i0116"]"

# afficher une popup expliquant qu'il faut se connecter une première fois
# Et installer l'extension chrome pour retenir les users et password
def show_popup():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("Information", "Please connect for the first time and install the Chrome extension to remember the users and passwords.")
    root.destroy()


print ("Test if we need to wait the page of the user / password")
if tools.waitLoadingPageByID2(5, 'i0116') :
    show_popup()
    print ("Need to wait the page of the password")
    tools.waitLoadingPageByID2(10, 'i0118')
    print ("Need to wait the way of validation")
    tools.waitLoadingPageByID2(30, 'idDiv_SAOTCS_Title')
    print ("Need to wait validation")
    time.sleep(30)
    print ("Need to wait the installation of the extension") 
    time.sleep(30)
else :
    print ("No need to wait")

j.recoverJiraInformation()
# j.startJira()

# Create folder link to this JIRA
j.createFolderJira(j.jira)
j.createFileInto(j.jira, j.jiraTitle, j.description_text, j.jira, j.jira + "_Comment_v001")

# Update MyHours
# m.connectToMyHours()
# if isStartMyHoursNeeded != True :
#     m.enterCredentials()
# print ("Start Jira epic_link : " + j.epic_link)
# m.modifyTrack(j.jira, j.jira + ' - ' + j.jiraTitle, j.epic_link)
m.connectToMyHours()
# m.enterCredentials()
m.startTrackWithDescription(j.jira, j.jira + ' - ' + j.jiraTitle, j.epic_link)


# 
tools.openFolder(j.save_path + j.jira)
tools.openFile(j.save_path + j.jira + '/' + j.jira + '_Comment_v001.txt')

# Exit Chrome
tools.driver.quit()