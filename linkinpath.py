
# coding: utf-8

# In[25]:


from os import path
import glob


# In[26]:


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


# In[27]:


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


# In[28]:


def getHtmlFiles(fold):
    allfiles = getAllFiles(fold)
    fh = open(fold+"/links.json", "w")
    fh.write("data = [");
    for i in allfiles:
        if i.endswith(".html"):
            ld = "{\"link\":\""+i.replace(fold,"")+"\"},"
            fh.write(ld+"\n");
    fh.write("]")
    fh.close()
    #html


# In[29]:


fold = raw_input("enter the path of root folder\n '\\' wont work, use '/' instead.\n")
getHtmlFiles(fold)

