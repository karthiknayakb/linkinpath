
# coding: utf-8

# In[124]:


from os import path
import glob


# In[125]:


def getFileFolders(p):
    files=[];
    folders=[];
    p.replace("\\","/");
    p+="/*";
    res = glob.glob(p)
    for i in res:
        if path.isdir(i):
            folders.append(i.replace("\\","/"))
        elif path.isfile(i):
            files.append(i.replace("\\","/"))
    return [files,folders];


# In[126]:


def getAllFiles(p):
    filefolders = getFileFolders(p)
    files = []
    folders = []
    files+=filefolders[0]
    folders+=filefolders[1]
    for i in folders:
        filefolders = getFileFolders(i)
        files+=filefolders[0]
        folders+=filefolders[1]
    return list(set(files))


# In[127]:


def getHtmlFiles(fold):
    allfiles = getAllFiles(fold)
    html=[]
    for i in allfiles:
        if i.endswith(".html"):
            html.append(i.replace(fold,""))
    fh = open(fold+"/links.txt", "w")
    for i in html:
        fh.write(i+"\n")
    fh.close()
    #html


# In[128]:


fold = raw_input("enter the path of root folder\n '\\' wont work, use '/' instead.")
getHtmlFiles(fold)

