import os  
from shutil import move as mve
from time import sleep as slp
import os

def IsItDirectory(Path2Backup, videoPathsinDirectory, photoPathsinDirectory):
    if os.path.isdir(Path2Backup):
        print("\nIt is a directory")
        getFilesinDirectory(Path2Backup, videoPathsinDirectory, photoPathsinDirectory)
    elif os.path.isfile(Path2Backup):
        print("\nIt is a normal file")
        if Path2Backup.upper().endswith('.MOV') or Path2Backup.upper().endswith('.MPEG-1') or Path2Backup.upper().endswith('.MPEG-1') or Path2Backup.upper().endswith('.MP4') or Path2Backup.upper().endswith('.MPG'):
            videoPathsinDirectory.append(Path2Backup)
        elif Path2Backup.upper().endswith('.jpg') or Path2Backup.upper().endswith('.png') or Path2Backup.upper().endswith('.gif'):
            photoPathsinDirectory.append(Path2Backup)
    else:
        print("It is a special file (socket, FIFO, device file)" )
    print()

 
def getFilesinDirectory(Path2Backup, videoPathsinDirectory, photoPathsinDirectory):
    executionCurrentDirectory = os.getcwd()
    #print(executionCurrentDirectory)
    os.chdir(Path2Backup)
    files = os.listdir(Path2Backup)
    
    for f in files:
        #print(Path2Backup + "\\" + f)
        if f.upper().endswith('.tmp'):
            break            
        if f.upper().endswith('.MOV') or f.upper().endswith('.MPEG-1') or f.upper().endswith('.MPEG-1') or f.upper().endswith('.MP4') or f.upper().endswith('.MPG'):
            videoPathsinDirectory.append(Path2Backup + "\\" + f)
        elif f.upper().endswith('.jpg') or f.upper().endswith('.png') or f.upper().endswith('.gif'):
            photoPathsinDirectory.append(Path2Backup + "\\" + f)
        elif os.path.isdir(f):
            getFilesinDirectory(Path2Backup + "\\" + f, videoPathsinDirectory, photoPathsinDirectory)
        elif f.upper().endswith('.tmp'):
            break

        # if f.upper().endswith('.zip'):
        # elif f.upper().endswith('.MOV') or f.upper().endswith('.MPEG-1') or f.upper().endswith('.MPEG-1') or f.upper().endswith('.MP4') or f.upper().endswith('.MPG'):
            # videoPathsinDirectory.append(f)
        # elif f.upper().endswith('.pdf') or f.upper().endswith('.docx') or f.upper().endswith('.doc') or f.upper().endswith('.ppt') or f.upper().endswith('.pptx'):
        # elif f.upper().endswith('.jpg') or f.upper().endswith('.png'):
            # photoPathsinDirectory.append(f)
        # elif f.upper().endswith('.tmp'):
            # break
        # elif os.path.isdir(f):
            # getFilesinDirectory(f, videoPathsinDirectory, photoPathsinDirectory)
        # elif not os.path.isdir(f):
    #slp(10)
    os.chdir(executionCurrentDirectory)