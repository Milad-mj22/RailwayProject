import os
import sys
import ctypes
import win32net
import win32netcon
import win32security
import ntsecuritycon as con


PERMITION = {
            'Everyone': con.FILE_GENERIC_READ | con.FILE_GENERIC_WRITE | con.FILE_GENERIC_EXECUTE | con.FILE_ALL_ACCESS | con.FILE_DELETE_CHILD 
            }

class fileManager:

    

    @staticmethod
    def build_dir(path):
        base_path = os.path.dirname(path)
        #sub_path = os.path.basename(path)
        if (not os.path.isdir(base_path)) and base_path != '':
            fileManager.build_dir(base_path)

        if (not os.path.isdir(path)) and path !='' :
            os.mkdir(path)



    @staticmethod
    def delete_file(path):
        os.remove(path)



    @staticmethod
    def create_and_share_folder(folder_path, share_name, description="", permissions=None):
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Define the share info
        share_info = {
            'netname': share_name,
            'type': win32netcon.STYPE_DISKTREE,
            'remark': description,
            'permissions': 0,
            'max_uses': -1,
            'current_uses': 0,
            'path': folder_path,
            'passwd': ''
        }
        
        # Add the share
        win32net.NetShareAdd(None, 2, share_info)
        
        # Set folder permissions
        if permissions:
            fileManager.set_folder_permissions(folder_path, permissions)

    @staticmethod
    def remove_share(share_name):
        try:
            # Remove the share
            win32net.NetShareDel(None, share_name)
            print(f"Share '{share_name}' removed successfully.")
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def set_folder_permissions(folder_path, permissions):
        
        
        # Get the security descriptor for the folder
        sd = win32security.GetFileSecurity(folder_path, win32security.DACL_SECURITY_INFORMATION)
        dacl = sd.GetSecurityDescriptorDacl()
        
        # Add the specified permissions
        for user, access in permissions.items():
            user, domain, type = win32security.LookupAccountName("", user)
            dacl.AddAccessAllowedAce(win32security.ACL_REVISION, access, user)
        
        # Set the new DACL
        sd.SetSecurityDescriptorDacl(1, dacl, 0)
        win32security.SetFileSecurity(folder_path, win32security.DACL_SECURITY_INFORMATION, sd)

if __name__ == "__main__":
    folder_path = r'C:\SharedFolder'
    share_name = 'SharedFolder'
    description = 'This is a shared folder'
    
    # Example permissions (grant full control to Everyone)
    permissions = {
        'Everyone': con.FILE_GENERIC_READ | con.FILE_GENERIC_WRITE | con.FILE_GENERIC_EXECUTE | con.FILE_ALL_ACCESS
    }

    fileManager.remove_share(share_name)
    
    fileManager.create_and_share_folder(folder_path, share_name, description, permissions)
    print(f"Folder '{folder_path}' shared as '{share_name}'")
