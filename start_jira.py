from Tools import tools_v000 as tools
from Jira import jira as j
from MyHours import myhours as m
import os
from os.path import dirname

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

# Start MyHours
# if isStartMyHoursNeeded == True :
#     m.connectToMyHours()
#     m.enterCredentials()
#     m.startTrack()
# else :
#     print ("Not needed to start the time")

# Jira part
# j.loginToJira(userJira, passJira)
j.connectToJiraInsim(j.jira, j.userInsim, j.userInsimPassword)
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