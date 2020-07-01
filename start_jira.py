from Tools import tools_v000 as tools
from Jira import jira as j
from MyHours import myhours as m
import os
from os.path import dirname

j.jira = 'TOS-2780'

# -10 for the name of this project Start_Jira
save_path = dirname(__file__)[ : -10]
propertiesFolder_path = save_path + "Properties"

j.save_path = tools.readProperty(propertiesFolder_path, 'Start_Jira', 'save_path=')

# Open Browser
tools.openBrowserChrome()

# Start MyHours
m.connectToMyHours()
m.enterCredentials()
m.startTrack()

# Jira part
j.connectToJira(j.jira)
j.recoverJiraInformation()
j.startJira()

# Create folder link to this JIRA
j.createFolderJira(j.jira)
j.createFileInto(j.jira, j.jiraTitle, j.description_text)

# Update MyHours
m.connectToMyHours()
m.modifyTrack(j.jira, j.jira + ' - ' + j.jiraTitle, j.epic_link)

# 
tools.openFolder(j.save_path + j.jira)
tools.openFile(j.save_path + j.jira + '/' + j.jira + '_Comment_v001.txt')

# Exit Chrome
tools.driver.quit()