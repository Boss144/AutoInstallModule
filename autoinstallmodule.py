import subprocess
import tkinter as tk

def install_libraries():
    libraries = entry.get()
    for library in libraries.split():
        try:
            __import__(library)
            print(f'{library} is already installed.')
        except ModuleNotFoundError:
            print(f'{library} is not installed. Installing...')
            result = subprocess.run(['pip', 'install', library], stdout=subprocess.PIPE)
            
            if result.returncode == 0:
                print(f'{library} installed successfully.')
            else:
                print(f'There was an error installing {library}.')
    
root = tk.Tk()
root.title('Library Installer')

label = tk.Label(root, text='Enter the names of the libraries to install (separated by spaces):')
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text='Install Libraries', command=install_libraries)
button.pack()

root.mainloop()
