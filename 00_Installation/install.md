#**Course 00: Software Installation**  
##Sunday August 28 2016


Objectives
----------

Each student should end up with a bundle of softwares which are needed in the
compulsory courses of the Cogmaster.

Important informations
----------------------

The **only** slot in the schedule dedicated to installation of softwares is on
Tuesday August 30 from 9:00 to 12:00. We will **not** answer installation
questions during the following Info 1 or Info 2 lectures. We will be reluctant to to help you if you were not attending on Tuesday morning.  

This evening, you have at least 2 important things to do:

 1. backup your computer before the installations
 2. free at least 5 GB on your hard drive

Some installations will require an internet access, login and password for the ENS wifi will be provided on Monday, don't forget to bring them on Tuesday morning.

Installation procedures have been succesfully tested on computers running Windows (7 64bits), MacOS
(10.9 Maverick), and debian-based linux (Debian 8 Jessie 64bits). We have have few years of experience with usual install problems on various Operating System versions (Mac OS 10.6 to 10.11, Windows XP, 8 and 10, various linux flavors), but there are always some computers on which the usual procedures and fixes fail. We will try our best, if it happens to you, please be patient.

Non-standard equipement (typically tablets or some mini-PC) or OS (Chrome, iOS,...) are not supported.

If you are using Windows 10, make sure your user name doesn't include characters that don't belong to the english alphabet (accents, ideograms,...).

The download and installation instructions are specified below. Before Tuesday morning, unless you have an unsupported equipement or OS or don't have access to internet, or don't own a laptop, please download the software installers. The ENS wifi is usually very slow and prone to disconnections.

If you are using a debian-based Linux distribution, most of the install will be made using the `apt` package manager, thus is way safer to try the installation at your home than at the ENS if you have a decent internet connection.

You migh skip the `Atom` download and install if you are already using an advanced text editor such as wim, emacs, sublimetext...  
Beware: Microsoft Office Word, LibreOffice and other document formatting softwares are **not** text editors.

Download instructions
---------------------

When you download an installer file for a software, it is very important to:

1. make sure you know in which folder the instaler file is saved
2. just download the file, not execute it, so please de-activate any internet browser preference that would automatically execute a file upon download completion, and for Windows users, make sure you always select the `save the file as` option when the usual dialog window pops up for a download.

Select the download instructions for your operating system:  
[Downloads for Windows](#downloads-for-windows)  
[Downloads for Mac OS](#downloads-for-mac-os)  
[Downloads for Debian based Linux](#downloads-for-debian-based-linux)

Installation instructions
-------------------------

First, read the installation instructions relative to your operating system. Yes, I mean it, read all the installation instructions before trying to install anything.

Now, if what you've just read makes sense, you can try to install the softwares by following carefully the instructions **step by step, not skipping any**.

If you feel unsure, don't worry, just wait until Tuesday morning for the installation.

Some installations, especially components for pygame on Mac OS, are rather tricky, If you are not 100% sure of what some instruction for one step means, stop right before this step. It is much easier to prevent a misinstallation than to fix it. Don't install anything after this step as there are some dependencies.

Same if something does not work as expected, stop there and ask for our help on Tuesday morning.

Select the installation instructions for your operating system:  
[Installations for Windows](#installations-for-windows)  
[Installations for Mac OS](#installations-for-mac-os)  
[Installations for Debian based Linux](#installations-for-debian-based-linux)  

Once the installation on your computer completed, you can get some reading material from the teachers (you will be able to get if on the following courses if you succesfully installed everything at home and thus don't need to come tomorrow morning)

__________________________________________________

## Downloads for Windows

First, you need to know whether you are using a 64 bits or a 32 bits version of Windows,
follow the instructions [on this website](http://www.howtogeek.com/howto/21726/how-do-i-know-if-im-running-32-bit-or-64-bit-windows-answers/)

If you are using windows 7 or earlier, it will be useful to know the full name of your files, so open a file explorer (window key + e), then select the `Organize` menu, then `Folder and search options`, then the second tab `View`, uncheck the box `Hide extensions for known file types`, and finally click the `OK` button.

### Scratch
* To download the Scratch installer file `ScratchInstaller1.4.exe`, click on [this link](http://download.scratch.mit.edu/ScratchInstaller1.4.exe) or use a right click and the option `Save target as`, then select an appropriate directory, for example the default `Downloads` folder. You can alternatively download the installer file directly from the webpage http://download.scratch.mit.edu/

### Text Editor
* If you are using a 64 bits version of Window
 * download the Atom installer file `AtomSetup.exe`, use [this link](https://atom.io/download/windows). You can alternatively download the installer file directly by clicking on the big red `Download Windows Installer` button on http://atom.io
* If you are using a 32 bits version of Windows
 * download the Sublime Text installer `Sublime Text Build 3114 Setup.exe` using [this link](https://download.sublimetext.com/Sublime%20Text%20Build%203114%20Setup.exe)
 or directly from http://www.sublimetext.com/3.

### R and RStudio
* Download the lattest R package installer `R-3.3.1-win.exe` using [this link](https://cran.rstudio.com/bin/windows/base/R-3.3.1-win.exe) or directly from https://cran.rstudio.com/bin/windows/base/
* Download the lattest RStudio installer `RStudio-0.99.903.exe` using [this link](https://download1.rstudio.org/RStudio-0.99.903.exe) or directly from https://www.rstudio.com/products/rstudio/download/

### Git
* If you are using a 64 bits version of Window
 * Download the lattest `GitHub Desktop` installer using [this link](https://github-windows.s3.amazonaws.com/GitHubSetup.exe) or directly from http://desktop.github.com by clicking on the `Download GitHub Desktop` button
* If you are using a 32 bits version of Windows
 * download the git-for-windows installer `Git-2.9.3.2-32-bit.exe` using [this link](https://github.com/git-for-windows/git/releases/download/v2.9.3.windows.2/Git-2.9.3.2-32-bit.exe)
 or directly from the `Download` button on https://git-for-windows.github.io/

### Python documentation
* Download the archive of the official python documentation `python-2.7.12-docs-html.zip` with [this link](https://docs.python.org/2.7/archives/python-2.7.12-docs-html.zip) from https://docs.python.org/2.7/download.html, where you can also download a pdf version if you prefer.

### Python
* If you have a 64 bits Windows, download the Windows 64-Bit Python 2.7 Graphical Installer `Anaconda2-4.1.1-Windows-x86_64.exe` from [this link](https://repo.continuum.io/archive/Anaconda2-4.1.1-Windows-x86_64.exe) of directly from https://www.continuum.io/downloads
* If you have a 32 bit Windows XP, then download instead the Windows 32-Bit Python 2.7 Graphical Installer `Anaconda2-4.1.1-Windows-x86.exe` from [this link](https://repo.continuum.io/archive/Anaconda2-4.1.1-Windows-x86.exe) or directly from https://www.continuum.io/downloads

__________________________________________________

## Downloads for Mac OS

### Warming up

0. Make sure you know the administrator password for your computer (the password of your main account, i.e. the one you use to install new software) and that you are able to type blind (i.e. even if you don't see little stars for each character).

1. Know you system version, so you can chose which file to download
 * First go to the "apple" menu by clicking on the apple icon at the upper-left corner of the screen.
 * Select "About This Mac", and look at the Version number, the first two numbers are the major releases:

  | 10.4 | 10.5 | 10.6 | 10.7 | 10.8 | 10.9 | 10.10 | 10.11 |
  |------|------|------|------|------|------|-------|-------|
  | Tiger | Leopard | Snow Leopard | Lion | Mountain Lion | Mavericks | Yosemite | El Capitan |
  | 2005 | 2007 | 2009 | 2011 | 2012 | 2013 | 2014 | 2015 |
 * Check that your version of Mac OS X is 10.9 or higher (for example 10.9.5 or 10.11.2 are higher, but 10.6.10 is lower).  
 If not or if you can't or don't want to risk an upgrade this evening, or if you are not sure, **stop right now, don't download or install anything, and come see us tomorrow at 9:00 am**: you might be in one of the most complicated situations regarding software installations.

### XQuartz
* Download `XQuartz-2.7.9.dmg` by clicking on [this link](https://dl.bintray.com/xquartz/downloads/XQuartz-2.7.9.dmg) or from https://www.xquartz.org

### Python documentation
* Download the archive of the official python documentation `python-2.7.12-docs-html.zip` with [this link](https://docs.python.org/2.7/archives/python-2.7.12-docs-html.zip) from https://docs.python.org/2.7/download.html, where you can also download a pdf version if you prefer.

### Python
 * Download the Python 2.7 Graphical Installer for Mac OS X from the Anaconda distribution with [this link](https://repo.continuum.io/archive/Anaconda2-4.1.1-MacOSX-x86_64.pkg), or from http://continuum.io/downloads but then beware of selecting the correct version

### Git
 * Download the installer with [this link](https://central.github.com/mac/latest), or go to the webpage http://desktop.github.com and click on the `Download GitHub Desktop` button.

### Atom
 * Download the Atom installer by clicking on [this link](https://atom.io/download/mac), or on the big red `Download For Mac` button on the webpage [http://atom.io]

### Scratch
 * To download the Scratch installer file `MacScratch1.4.dmg`, click on [this link](http://download.scratch.mit.edu/MacScratch1.4.dmg) or use a right click and the option `Save target as`, then select an appropriate directory, for example the default `Downloads` folder. You can alternatively download the installer file directly from the webpage https://scratch.mit.edu/scratch_1.4/

### R and RStudio
 * Download the lattest R package installer `R-3.3.1.pkg` using [this link](https://cran.rstudio.com/bin/macosx/R-3.3.1.pkg) or directly from https://cran.rstudio.com/bin/macosx/
 * Download the lattest RStudio installer `RStudio-0.99.903.dmg` using [this link](https://download1.rstudio.org/RStudio-0.99.903.dmg) or directly from https://www.rstudio.com/products/rstudio/download/

### Command Line Tools
  * open a terminal: click on `Application` icon in your dock, then on the `Utilities` icon, then on the `Terminal` icon. Alternatively, you can open a `Finder` window and select the `Application` folder, then the `Utilities` folder, then double-click on the `Terminal` icon. You can also type `terminal` in the Spotlight search.
  * in this terminal window, copy and paste the following text then press on the `Enter` key (from now on this will be called **executing a command in the terminal**)

    ```
    xcode-select --install
    ```

  * this should make a window pop up to ask you if you want to install the "Command Line Tools", answer `Yes`, you might have to type your password, then wait until completion of the installation

  * If you can't perform this step, don't worry, come at 9:00 on Tuesday, we will help you do it.

__________________________________________________

## Downloads for Debian based Linux

First of all, you must determine if your system is 32 or 64 bits. Open
a terminal (Ctrl-Alt-T) and type the command

```
arch
```

If you see `x86_64`, your operating system is 64 bits, if you see
`i386` or `i686`, it is 32 bits.

### Text Editor

Note: If you are already using a decent text editor under linux
(gedit, emacs, vim,...) you won't need Atom.

 * if your linux is 64 bits, download `atom-amd64.deb` package from
[this link](https://atom.io/download/deb) or from the webpage https://github.com/atom/atom/releases/latest
 * if your linux is 32 bits, download the latest build package (currently 3114) from
[this link](https://download.sublimetext.com/sublime-text_build-3114_i386.deb) or the `Ubuntu 32 bits` link on https://www.sublimetext.com/3

### Python documentation
  * Download the archive of the official python documentation `python-2.7.12-docs-html.zip` with [this link](https://docs.python.org/2.7/archives/python-2.7.12-docs-html.zip) from https://docs.python.org/2.7/download.html, where you can also download a pdf version if you prefer.

### Python2.7
 * if your linux is 64 bits, download the install script `Anaconda2-4.1.1-Linux-x86_64.sh` using
[this link](https://repo.continuum.io/archive/Anaconda2-4.1.1-Linux-x86_64.sh) or from the webpage https://www.continuum.io/downloads, selecting the correct installer for Python2.7 and your version of linux
 * if your linux is 32 bits, download the install script `Anaconda2-4.1.1-Linux-x86.sh` using
[this link](https://repo.continuum.io/archive/Anaconda2-4.1.1-Linux-x86.sh) or from the webpage https://www.continuum.io/downloads, selecting the correct installer for Python2.7 and your version of linux

### Rstudio
 * if your linux is 64 bits, download the package `rstudio-0.99.903-amd64.deb` using
[this link](https://download1.rstudio.org/rstudio-0.99.903-amd64.deb) or from the webpage https://www.rstudio.com/products/rstudio/download3/
 * if your linux is 32 bits, download the package `rstudio-0.99.903-i386.deb` using
[this link](https://download1.rstudio.org/rstudio-0.99.903-i386.deb) or from the webpage https://www.rstudio.com/products/rstudio/download3/

__________________________________________________







## Installations for Windows

### Scratch
 1. Open a file explorer (windows key + e) and open the directory in which you downloaded the installer file `ScratchInstaller1.4.exe`, typically the default `Downloads` directory.
 2. then execute the installer:
  * double-click on the `ScratchInstaller1.4.exe` file and wait
  * after a while your screen turns dark and an ominous warning pop-up window ask you if you'd like this unknown programm to modify stuff on your computer. Click on the `Yes` button.
  * The Scratch Setup Wizard window should pop-up and you can install the software clicking on the `Next` Button and accepting default parameters (note in which directory the program will be installed) until you have to click on the `Finish` button.
 3. test Scratch
  * If you did not uncheck the options before clicking on `Finish`, you should see the program running and you coud reopen it using the desktop Scratch icon. Alternatively, you can open an explorer, go to the directory in which the program was installed and double click on the Scratch icon.
  * you should be able to move the little animal around

### R and RStudio

 1. Installation
  * open a file explorer (windows key + e) and open the directory in which you downloaded the installer file `R-3.3.1-win.exe`.
  * install R by double-clicking on the downloaded file and following the steps on the typical Windows installer pop-up windows (as usual, you just have to click on `Install`, then `Yes` to "Allow modifications by an unknown program editor", then agree with the licence agreement if needed, then click the `Next` and/or `Finish` buttons using either default options or a different option when instructed to do so as you can see on the next lines).
  * when asked to "Select Start Menu ", check the `Don't create a Start Menu folder`, as we will use RStudio by default
  * when asked to "Select Additional Tasks", uncheck the `Create a desktop icon`, for the same reason
  * then install RStudio by double-clicking on the `RStudio-0.99.903.exe` icon in your the download directory. It should be straight forward as you know the usual install process now.

 2. Verification
  * if you want to create a RStudio desktop icon, open the Windows Start Menu by clicking on the taskbar window icon or hitting the windows key on your keyboard, look for the RStudio program icon, then drag and drop the RStudio icon to your desktop.
  * launch RStudio from the Windows Start Menu or with a double click the icon on your desktop, or using the search or side panel for Windows 8 users
  * in the `Console` panel, type 'demo(graphics)' and hit the `Enter` key


### Git
0. Set up an account on Github.com
  * Open an internet browser and go to http://github.com
  * fill the requested fields with appropriate username, email, and password
  * click on the `Sign up for Github` button
1. Installations
  + If you are usign a 64 bits version of Windows
    1. Installation
      * go to the directory where you donloaded the installer `GitHubSetup.exe`
      * then double-click  on the file installer icon to start the install process. It will download some    mofiles, be patient.
      * when it's done, you should see a window that says "Welcome"
    2. Configuration:
      * fill the username and password and click on `login`, then your email and click on `Continue`
      * skip the local repository search
      * now you can just quit the "Github Desktop" application
  + If you are using a 32 bits version of Windows
    1. Installation
      * go to the directory where you donloaded the installer `Git-2.9.2-32-bit.exe`
      * then double-click  on the file installer icon.
      * check the `Additional icons > On the Desktop` option to get an easy access to the program
      * when asked about further options, use the default choice
    2. Configuration
      * go to your desktop and  open the `Git Bash` terminal window with a double-click on the icon
      * configure your identity, by typing in the `Git Bash` terminal window the following line with the user name of your GitHub account,then hitting the `Enter` key
      ```
      git config --global user.name "your_user_name"
      ```
      * configure your email, by typing in the `Git Bash` terminal window the following line with the email associated with your GitHubaccount, then hitting the `Enter` key
      ```
      git config --global user.email your_email@example.com
      ```

    * you can close the `Git Bash` window now.

### Text Editor

* If you are using a 64 bits version of Windows, install `atom`
 * use a file explorer (windows key + e) to open the directory in which you downloaded the installer file `AtomSetup.exe`
 * double-clicking on the installer file icon
 * if a pop-up dialog window ask you to install the `.NET Framework`, proceed by clicking on the `Install` button, then accept the installation and wait for the files to be downloaded and installed

* If you are using a 32 bits version of Windows, install `Sublime Text`
 * use a file explorer (windows key + e) to open the directory in which you downloaded the installer file `Sublime Text Build 3114 Setup.exe`
 * double-clicking on the installer file icon, then follow the install process, changing only one option:
 * when asked to `Select Additional Tasks`, check the option `Add to explorer context menu`


### Python documentation

 * use a right-click on the archive then select the `Extract all` option
 * select the directory in which you would like to put the documentation
 * then click on the `Extract` button on the bottom right of the next window.

### Python

1. Installation of the Anaconda distribution
 * go to your download folder and double click on the Anaconda2 file installer icon to initiate the installation process
 * on the Anaconda Setup Wizard, beware, pay attention to the following options option:
 * verify that you Install for `Just Me (recommended)`, then click on `Next`
 * use default Destination folder and click on `Next`
 * check that both "Add Anaconda to my PATH" and "Register Anaconda as my default Python 2.7" are ckecked and click on `Install`
 * upon completion, click on 'Next', then `Finish`
2. Test
 * click on the windows icon on the left bottom of your screen. For windows 8 early version users, use your search command to find the application using its name.
 * click on `All the programs` and then the `Anaconda (64-bit)` folder, what you are looking for is the `IPython (Py 2.7)` entry. Click there (and not the `IPython (Py 2.7) Notebook` nor the `IPython (Py 2.7) QTConsole`).
 * this launches a window that understands only commands in the python language
 * in just after the `$` sign, type each of those lines one by one followed by a stroke on the `Enter` key
 ```
 import numpy as np
 import matplotlib.pyplot as plt
 from scipy import stats
 x=np.arange(-5,5,.1)
 y=stats.norm.pdf(x)
 plt.plot(x,y)
 plt.show()
 ```
 * close the window with the graph
 * close the ipython shell by typing `quit()` or the keyboard shortcut `ctrl + D`
3. Installing pygame
 * click on the windows icon on the left bottom of your screen. For windows 8 early version users, use your search command to find the application using its name.
 * click on `All the programs` and then the `Anaconda2 64bits` folder, then on `Anaconda Prompt`
 * this launches the anaconda terminal
 * notice a little rectangle is blinking after something that looks like `C:Users\user_name\AppData\Local\Continuum\Anaconda2>`?   
 This is call a "prompt" and it means you can type some text there to interract with your computer
 * at the prompt, type the following text and then press on the `Enter` key (this is called "executing a command", more on that in the first Info lectures!):
 ```
 conda install conda
 ```
 * you will see some text messages during the installation of some python modules, don't worry!
 * when you are asked `Procced ([y]/n)`, press on the `Enter` key (because yes is the default)
 * when you are back to the blinking little rectangle, type this text, then press the `Enter` key:
 ```
 conda install -c cogsci pygame=1.9.2a0
 ```
 * When the installation of pygame is over, you can even type `exit` and press on `Enter` to close the window, how convenient!
4. Testing pygame
  1. First test
    * click on the windows icon on the left bottom of your screen. For windows 8 early version users, use your search command fo find the application  using its name.
    * click on `All the programs` and then the `Anaconda2 64 bits` folder, then on `Ipython`
    * after the "IPython window" has opened, you can copy and paste the following seven lines just after the `In [1]:`, then press twice on `Enter`
     ```
     import pygame
     pygame.init()
     w=pygame.display.set_mode([300,300])
     w.fill([128,37,213])
     pygame.display.flip()
     pygame.time.wait(3000)
     pygame.quit()
     ```
    * You should see a little window appear, change color and then disappear (if it doesn't disappear, hit the `Enter` key).
    * press the keys `ctrl+D` and confirm your will to exit in order to quit the ipython console
    * if all these terms "console", "command", "prompt", "anaconda", or the difference between python and "ipython" seems rather confusing, don't worry, the first Info lectures will help you.
  2. Second test
    * click on the `Windows` icon (or just press the `Windows` key on your keyboard), then on `All the programs` and then the `Anaconda2 64bits` folder, then on  `Anaconda Prompt`
    * at the prompt, type the following text, with the correct user name then press on `Enter`
     ```
     python C:Users\user_name\AppData\Local\Continuum\Anaconda2\Lib\site-packages\pygame\examples\chimp.py
     ```
     You should be able to play a silly little game, including sound (make sure the sound is on, but not too loud).
5. Installing expyriment
  1. Launch the anaconda terminal
    * click on the windows icon on the left bottom of your screen. For windows 8 early version users, use your search command to find the application using its name.
    * click on `All the programs` and then the `Anaconda folder`, then on `Anaconda Command Prompt`
  2. execute the following command (type the text, then press on the `Enter` key):
  ```
  pip install expyriment
  ```
6. Testing expyriment
  1. Launch the ipython console as you did in the 4th step (`Window` icon, `All the programs` and then the `Anaconda2 64 bits` folder, then on `Ipython`).  
  You should see the `In [1]: ` and the blinking cursor after which you can start typing.
  2. In the console, type or copy paste the following lines one by one
  ```
  import expyriment
  ```
  ```
  exp = expyriment.design.Experiment(name="test")
  ```
  ```
  expyriment.control.initialize(exp)
  ```
  3. You should now see this message:
  ```
  Python is running in an interactive shell but Expyriment wants to initialize a fullscreen  
  Do you want to switch to windows mode? (Y/n)
  ```
  4. Confirm the switch to a windowed mode by hitting the `Enter` key (Y is in uppercase to show it's the default option, you can also type "yes" then hit `Enter`).
  5. Then you should see the expyriment window appear and do its stuff ("preparing expyriment...") until the "Preparing experiment..." message is displayed
  6. Select the python window and execute the following command:
  ```
  expyriment.control.start()
  ```
  7. Then you should select the expyriment window and hit `Enter` to validate the subject number.  
  The windows should now diplay "Ready". Hit `Enter` a second time to validate.
  8. Select the python window, you should see the `In [X]: ` and the blinking cursor after which you can start typing, then execute the following command:
  ```
  expyriment.control.end()
  ```
  If this doesn't close the expyriment window, hit the `Enter` key once more.  
  Now you can exit the python command line using `Ctrl+d` and `Enter`.

__________________________________________________






## Installations for Mac OS

### Configuration
 * make sure you know the administrator password for your computer (password used to install new software) and that you are able to type it blind.
 * click on the `Finder` icon on your dock then click on the `Finder` text next to the `Apple` logo on the top left corner of your screen to get the menus, then on `Preferences`, then on the `Side Bar` tab, check the first unchecked box under `DEVICES`. Now you can close the `Finder Preferences` window.
 * click on the apple logo on the top left of your screen, then on `System Preferences`, the select the `Security & Privacy` icon and on the `General` tab, select the option `Anywhere` regarding `Allow apps downloaded from:`. You might have to click on the littke locker icon on the bottom left of the window and type your pasword if your preferences are protected.
 * open a `Finder` window and select the `Application` folder, then the `Utilities` folder, then drag the `Terminal` icon and drop it on the second position of your "Dock", right after the `Finder` icon. No you have and easy access to the most powerful application of your mac.

### XQuartz
* Installation
 * double click on `XQuartz-2.7.9.dmg` in your `Downloads` folder or wherever you downloaded it.
 * double click on the `XQuartz.pkg`
 * click on `Continue` and `Agree` until you can click on `Install`

### Git
0. Set up an account on Github.com
 * Open an internet browser and go to [http://github.com]
 * fill the requested fields with appropriate username, email, and password
 * click on the `Sign up for Github` button
2. Installation
 * Go to your `Downloads` folder
 * decompress the `.zip` archive if needed by double-cliking its icon
 * double-click on the `GitHub Desktop.app` icon
 * click on the `Open` button at the security pop up window
 * click on `Move to Application Folder`
3. configuration: you should see a window that says "Let's take a minute to setup your computer"
 * click on `Continue`
 * fill the username and password and click on `Sign up`, then on `Continue`
 * Click on `Install Command Line Tools`, then on the pop-up window, type down your mac account password and click on `Install Helper`
 * click on `OK` upon completion of the Helper install
 * Then click on `Continue` on the "Welcome to GitHub Desktop"
 * Don't add any repository yet, just click on `Done`
 * now you can just quit the "Github Desktop" application


### Atom
 * Go to your `Downloads` folder
 * decompress the `.zip` archive if needed by double-cliking its icon
 * drag the `GitHub Desktop.app` and drop it in your `Application` Folder


### Scratch
1. Install `MacScratch1.4.dmg` as usual:
 * select your `Downloads` folder from the `Dock`
 * clic on the .dmg file to mount the virtual disk that wraps the application
 * drag and drop this application to your `Applications` folder in the pop-up window
 * eject the virtual disk
3. test Scratch
 * select your `Applications` folder from the `Dock`
 * clic on the `Scratch1.4` folder
 * then clic on the `Scratch.app` icon
 * the Scratch window should appear on your screen and you should be able to drag and move the little animal around

### R and RStudio
1. R installation
 * in the Finder open the folder in which you downloaded the `R-3.3.1.pkg` R package
 * double-click on the package icon
 * the package installer window will open, click on `Next`
 * `Agree` to the terms of the licence
 * select the `Install for all users of this computer` option and click on `Continue`
 * click on `Install`

2. RStudio installation
 * go to the download folder then double-click on `RStudio-0.99.093.dmg`. In the window that pops up, slide the RStudio icon into the Applications folder

3. Verification
 * Launch RStudio from the icon on your desktop
 * in the `Console` panel, type

    ```
     demo(graphics)
    ```

then, hit the `Enter` key.

### Python documentation

 * use a double-click on the archive `python-2.7.12-docs-html.zip`, this automatically extract the archive content in a folder
 * use your finder to select (and create if needed) the directory in which you would like to put the documentation
 * drag and drop the created folder in this new directoru


### Python
1. Install the Anaconda python distribution
 * go to your `Downloads` folder and double click on the file `Anaconda2-4.1.1-MacOSX-x86_64.pkg` in order to start the installation.
 * click on `Continue` several times and `Agree` on licence terms until the installation is completed, if at some point you see the error "You cannot install Anaconda in this location", then just click on `Install for me only` and you should be able to continue.
 * when you see the message "The installation was successful", click on the `Close` button

2. Test python
 * lauch the `Terminal` application from your "Dock"
 * just after the `$` sign, type `ipython` then press on the `Enter` key in order to lauch a ipython interpreter
 * in the ipython shell, type each of those lines one by one followed by enter

    ```
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import stats
    x=np.arange(-5,5,.1)
    y=stats.norm.pdf(x)
    plt.plot(x,y)
    plt.show()
    ```
 * close the window with the graph
 * close the ipython shell by typing `quit()` or the keyboard shortcut `ctrl + D`
 * you are now back to the command line in the Terminal application.

3. **Warning** Now the Mac python install procedure starts to be tricky, if you don't feel confident with typing commands in a terminal, of if you'd like to sleep, stop rigth now, we will carry on Tuesday morning.  
Otherwise, stay up for some more fun with the terminal!

4. Install "Homebrew
 * in a terminal, copy paste or type this command:
     ```
     /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
     ```

 * if you ever have an error about certificates using `curl`, execute the two following commands and restart the "Homebrew" install of the previous step
     ```
     export CURL_CA_BUNDLE=/usr/local/curl/
     curl http://curl.haxx.se/ca/cacert.pem -o cacert.pem
     ```

 * wait...
 * once the installation is over type in the terminal
     ```
     brew doctor
     ```

 * wait...
 * when the doctor gave you its check-up diagnosis, it should tell you that your system is ready for brewing stuff or something similar  
       **IF THERE IS SOME CRITICAL ERROR AND NOT JUST WARNINGS, STOP THE INSTALLATION PROCESS NOW AND ASK US WHAT TO DO**

 * **If and only if** the doctor gave its green light, you can Now close (by typing `exit` and then closing the windows with the `cmd+W` key stroke combination) all your instances of the terminal application, quit the application `cmd+Q` and relaunch it.

5. Install pygame dependencies
 * with the following command:
     ```
     brew install sdl sdl_image sdl_mixer sdl_ttf portmidi
     ```
 * wait

9. Install "conda"
 * In a terminal, execute
     ```
     conda install conda
     ```

 * when you are asked `Procced ([y]/n)`, press on the `Enter` key (because yes is the default
 * wait


10. Finally install pygame
 * by typing in the terminal
     ```
     conda install -c cogsci pygame=1.9.2a0
     ```

 * when you are asked `Procced ([y]/n)`, press on the `Enter` key (because yes is the default
 * wait

11. Check the installation
 * in a terminal, type
     ```
     ipython
     ```

 * after the "IPython window" has opened, you can copy and paste the following seven lines just after the `In [1]:`, then press twice on `Enter`
     ```
     import pygame
     pygame.init()
     w=pygame.display.set_mode([300,300])
     w.fill([128,37,213])
     pygame.display.flip()
     pygame.time.wait(3000)
     pygame.quit()
     ```
 * press the keys `ctrl+D` to quit the ipython console, you should be back to the standard terminal (you should see `--bash--` on the top of the terminal window)
 * to further check the installation, in a this terminal window, first, look for the place where the `chimp.py` file is located in the hierarchy of folders within the anaconda installation:
 ```
 find ~/anaconda*/lib -name "chimp.py"
 ```
 * you should see one line explicitely describing the succession of the directories from `/Users` to the file `chimp.py` (we call that the "path" to the `chimp.py` file, more on that in the following courses)

 * then still in the terminal, execute the following command, replacing `the_line_with_the_succession_of_folders_that_ends_with_chimp.py` by the one you just found in the previous step (use copy and paste if needed)
 ```
 python the_line_with_the_succession_of_folders_that_ends_with_chimp.py
 ```

 * if you have trouble with the previous command execute the following command
    ```
    python $(find ~/anaconda* -name "chimp.py")
    ```

 * You should be able to play a silly game, including sound (make sure the sound is on, but not too loud).

12. Installing expyriment
  1. install expyriment from the terminal
     * launch a terminal if it's not done already
     * execute the following command (type the text, then press on the `Enter` key):
        ```
        pip install expyriment
        ```
  2. restart your session  
     * close the terminal by executing
     ```
     exit
     ```
     * quit the Terminal application, using the top menu `Terminal` > `Close Terminal` or the `CMD + Q` keyboard shortcut. You should not see the terminal anymore when navigating between applications using the `Alt + Tab` keyboard shortcut.

     * close your session using the `apple menu` (clic on the apple icon on the top left of your screen), then `Log Out your_user_name`, or using the `Shift Cmd Q` keyboard shortcut

13. Testing expyriment
     0. log in your session
     1. open a Terminal
     2. Launch the ipython console by executing the command
     ```
     ipython
     ```
     3. In this ipython console, once you see the `In [1]: ` and the blinking cursor, type or copy paste the following lines one by one

    ```
    import expyriment
    ```

    ```
    exp = expyriment.design.Experiment(name="test")
    ```

    ```
    expyriment.control.initialize(exp)
    ```

    Then you should see this message:  
    > Python is running in an interactive shell but Expyriment wants to initialize a fullscreen
    > Do you want to switch to windows mode? (Y/n)

    Confirm the switch to a windowed mode by hitting the `Enter` key (Y is in uppercase to show it's the default option, you can also type "yes" then hit `Enter`).

    Then you should see the expyriment window appear and do its stuff ("preparing expyriment...") until the "Ready" message is dosplayed

    ```
    expyriment.control.start()
    ```

    ```
    expyriment.control.end()
    ```

    If this doesn't work, turn your computer on and of again, then retest expyriment.

__________________________________________________








## Installations for Debian based Linux

## Text Editor

The `*.deb` files can be installed by simply clicking on them, or on
the command line, with the command `sudo dpkg -i`, e.g.:
```
sudo dpkg -i atom-amd64.deb
```

### Python documentation

In a terminal, go where you donloaded the `python-2.7.12-docs-html.zip` archive and type the following command, using the path to where you want to store the documentation files

```
unzip -d path_to_a_directory python-2.7.12-docs-html.zip
```

### Python

1. Install python 2.7
 * Open a terminal (Ctrl-Alt-T) and type:
```
bash ~/Downloads/Anaconda*.sh
```

 * **Note**: if you the installer is in a different folder than `Downloads`,
change to the correct path

2. Check the python installation
 * in a terminal, type `ipython` in order to lauch a ipython interpreter
 * in the ipython shell, type each of those lines one by one
followed by enter

```
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import stats
    x=np.arange(-5,5,.1)
    y=stats.norm.pdf(x)
    plt.plot(x,y)
    plt.show()
```

 * exit the ipython shell by typing `quit()` or the keyboard
shortcut `ctrl + D`

 * then you are back to the terminal shell where you can install pygame


3. Install Pygame
 * In a terminal, type
```
    conda install -c cogsci pygame=1.9.2a0
```

2. Check the pygame installation
 * in a terminal, type `ipython` in order to lauch a ipython interpreter
 * in the ipython shell, type each of those lines one by one
followed by enter

 1. First test
  * in a terminal, type `ipython` in order to lauch a ipython interpreter
  * then you can copy and paste the following seven lines just after the ipython prompt (`In [1]:`), then press twice on `Enter`

    ```
    import pygame
    pygame.init()
    w=pygame.display.set_mode([300,300])
    w.fill([128,37,213])
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    ```

    You should see a little window appear, change color and then disappear (if it doesn't disappear, hit the `Enter` key).
  * press the keys `ctrl+D` and confirm your will to exit in order to quit the ipython console

 2. Second test
  * open a terminal and look for the chimpy.py file in the anaconda hierarchy
  ```
  find ~/anaconda*/lib -name "chimp.py"
  ```
  * in a terminal, type `ipython` in order to lauch a ipython interpreter
  * at the prompt, type the following command, replacing path_to_chimp.py by the path you found with the `find` command, then press on `Enter`
      ```
      python path_to_chimp.py
      ```

      or

      ```
      python $(find ~/anaconda*/lib -name "chimp.py")
      ```

      You should be able to play a silly little game, including sound (make sure the sound is on, but not too loud).


3. Install expyriment
 * in a terminal, type
  ```
  pip install expyriment
  ```

4. Test expyriment
1. Launch the ipython console as you did before
2. In the console, type or copy paste the following lines one by one

```
import expyriment
```

```
exp = expyriment.design.Experiment(name="test")
```

```
expyriment.control.initialize(exp)
```

Then you should see this message:  
> Python is running in an interactive shell but Expyriment wants to initialize a fullscreen
> Do you want to switch to windows mode? (Y/n)

Confirm the switch to a windowed mode by hitting the `Enter` key (Y is in uppercase to show it's the default option, you can also type "yes" then hit `Enter`).

Then you should see the expyriment window appear and do its stuff ("preparing expyriment...") until the "Ready" message is dosplayed

```
expyriment.control.start()
```

```
expyriment.control.end()
```

You can now exit the ipython console


### Git
1. Download et installation

```
sudo apt-get install git-core
```

2. Configuration, by typing in a terminal with the appropriate replacements

```
git config --global user.name "your_user_name"
git config --global user.email your_email@example.com
```

### Scratch
1. Installation: in a terminal, type

```
sudo apt-get install scratch
```

2. Test : in the terminal of a graphic console, type

```
scratch
```

You should see a new window, where you should be able to grab and move
the little mascot.


### R

The instructions to install R are available here:
<https://cran.r-project.org/bin/linux/ubuntu/README.html#installation>

1. Setup
 * Check which linux exactly you are using with the following command

```
   lsb_release -da
```

You should see an output like this one:

```
    Distributor ID: Debian
    Description :   Debian GNU/Linux 7.8 (wheezy)
    Release:        7.8
    Codename:       wheezy
```

 * add the appropriate repository to your `/etc/apt/sources.list`

```
sudo sh -c 'echo deb http://cran.univ-paris1.fr/bin/linux/debian
wheezy-cran3/ >> /etc/apt/sources.list'
```

For Ubuntu, you migh have to leave out the -cran3 after the version codename

```
    sudo sh -c 'echo deb http://cran.univ-paris1.fr/bin/linux/ubuntu
vivid/ >> /etc/apt/sources.list'
```


 * update your repository list by executing

```
sudo apt-get update
```

2. Install R
* In a terminal, run the apt install command
```
sudo apt-get install r-base r-base-core r-base-html
```

### Rstudio
1. Installation
 * in a terminal, execute the following command, replacing the XX by the version numbers

```
    sudo apt-get install libjpeg62
    sudo dpkg -i rstudio-X.XX.XXX-amd64.deb
```

2. Verification
 * type `rstudio` in a console to lauch the R interpreter
 * type 'demo(graphics)' and press on 'Enter' to see the graphs.
