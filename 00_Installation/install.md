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
If you don't have a computer yet, tell us after the compulsory courses presentation on Monday August 29.

Backup your computer before the installations.
Free at least 5 GB on your hard drive.

Some installations will require an internet access, login and password for the ENS wifi will be provided on Monday, don't forget to bring them on Tuesday morning.

Installation procedures have been succesfully tested on computers running Windows (7 64bits), MacOS
(10.9 Maverick), and debian-based linux (Debian 8 Jessie 64bits). We have have few years of experience with usual install problems on various Operating System versions (Mac OS 10.6 to 10.11, Windows XP, 8 and 10, various linux flavors), but there are always some computers on which the usual procedures and fixes fail. We will try our best, if it happens to you, please be patient.

Non-standard equipement (typically tablets or some mini-PC) or OS (Chrome, iOS,...) are not supported.

If you are using Windows 10, make sure your user name doesn't include characters that don't belong to the english alphabet (accents, ideograms,...).

The download and installation instructions are specified below. Before Tuesday morning, unless you have an unsupported equipement or OS or don't have access to internet, please download the software installers. The ENS wifi is usually very slow and prone to disconnections.

If you are using a debian-based Linux distribution, there is no installer to download but the installations will be made with `apt`, thus is way safer to try the installation at your home than at the ENS if you have a decent internet connection.

You migh skip the `Atom` install if you are already using an advanced
text editor such as wim, emacs, sublimetext.  
Beware: Microsoft Office Word, LibreOffice and other document formatting softwares are **not** text editors.

Download instructions
---------------------

When you download an installer file for a software, it is very important to:

1. make sure you know in which folder the instaler file is saved
2. just download the file, not execute it, so please de-activate any internet browser preference that would automatically execute a file upon download completion, and for Windows users, make sure you always select the `save the file as` option when the usual dialog window pops up for a download.

Select the download instructions for your operating system:  
[Downloads for Mac OS](#downloads-for-mac-os)  
[Downloads for Windows](#downloads-for-windows)
[Downloads for Debian based Linux](#downloads-for-debian-based-linux)

Installation instructions
-------------------------

First, read the installation instructions. Yes, I mean it, read all the installation instructions before trying to install anything.

Now, if what you've just read makes sense, you can try to install the softwares by following carefully the instructions **step by step, not skipping any**.

If you feel unsure, don't worry, just wait until Tuesday morning for the installation.

Some installations, especially components for pygame on Mac OS, are rather tricky, If you are not 100% sure of what some instruction for one step means, stop right before this step. It is much easier to prevent a misinstallation than to fix it. Don't install anything after this step as there are some dependencies.

Same if something does not work as expected, stop there and ask for our help on Tuesday morning.

Select the installation instructions for your operating system:  
[Linux](#linux-debian-based)  
[Mac OS](#mac-os)  
[Windows](#windows)

Once the installation on your computer completed, you can browse the documents in [the ressource folder](../resources/)

__________________________________________________

## Downloads for Windows

First, you need to know whether you are using a 64 bits or a 32 bits version of Windows,
follow the instructions [on this website](http://www.howtogeek.com/howto/21726/how-do-i-know-if-im-running-32-bit-or-64-bit-windows-answers/)

If you are using windows 7, it might be useful to know the full name of your files, so open a file explorer (window + e), then select the `Organize` menu, then `Folder and search options`, then the second tab `View`, uncheck the

### Scratch
* To download the Scratch installer file `ScratchInstaller1.4.exe`, use a right click on [this link](http://download.scratch.mit.edu/ScratchInstaller1.4.exe) and the option `Save target as`, and select an appropriate directory, for example the default `Downloads` folder. You can alternatively download the installer file directly from the webpage http://download.scratch.mit.edu/

### Text Editor
* If you are using a 64 bits version of Window
 * download the Atom installer file `atom-windows.zip`, use a right click on [this link](https://github.com/atom/atom/releases/download/v1.9.9/atom-windows.zip) and the option `Save target as`, and select an appropriate directory, for example the default `Downloads` folder. You can alternatively download the installer file directly by clicking on the big red `Download Windows Installer` button on http://atom.io
* If you are using a 32 bits version of Windows
 * download the Sublime Text installer `Sublime Text Build 3114 Setup.exe` using [this link](https://download.sublimetext.com/Sublime%20Text%20Build%203114%20Setup.exe)
 or directly from http://www.sublimetext.com/3.

### R and Rstudio
  * Download the lattest R package installer `R-3.3.1-win.exe` using [this link](https://cran.rstudio.com/bin/windows/base/R-3.3.1-win.exe) or directly from https://cran.rstudio.com/bin/windows/base/
  * Download the lattest RStudio installer `RStudio-0.99.903.exe` using [this link](https://download1.rstudio.org/RStudio-0.99.903.exe) or directly from https://www.rstudio.com/products/rstudio/download/

### Git
* If you are using a 64 bits version of Window
Download the lattest `GitHub Desktop` installer using [this link](https://github-windows.s3.amazonaws.com/GitHubSetup.exe) or directly from http://desktop.github.com
* If you are using a 32 bits version of Windows
 * download the Sublime Text installer `Sublime Text Build 3114 Setup.exe` using [this link](https://download.sublimetext.com/Sublime%20Text%20Build%203114%20Setup.exe)
 or directly from http://www.sublimetext.com/3.

### Python
 * If you have a 64 bits Windows, download the Windows 64-Bit Python 2.7 Graphical Installer `Anaconda2-4.1.1-Windows-x86_64.exe` from [this link](https://repo.continuum.io/archive/Anaconda2-4.1.1-Windows-x86_64.exe) of directly from https://www.continuum.io/downloads
 * if you have a 32 bit Windows XP, then download instead the Windows 32-Bit Python 2.7 Graphical Installer `Anaconda2-4.1.1-Windows-x86.exe` from [this link](https://repo.continuum.io/archive/Anaconda2-4.1.1-Windows-x86.exe) or directly from https://www.continuum.io/downloads

### Python documentation
 * [this link](https://docs.python.org/2.7/archives/python-2.7.12-docs-html.zip) from https://docs.python.org/2.7/download.html

__________________________________________________

## Downloads for Mac OS

__________________________________________________

## Downloads for Debian based Linux

__________________________________________________

## Windows

### Scratch
1. Open a file explorer (windows key + e) and open the directory in which you downloaded the installer file `ScratchInstaller1.4.exe`, typically the default `Downloads` directory.
2. then execute the installer:
 * double-click on the `ScratchInstaller1.4.exe` file and wait
 * after a while your screen turns dark and an ominous warning pop-up window ask you if you'd like this unknown programm to modify stuff on your computer. Click on the `Yes` button.
 * The Scratch Setup Wizard window should pop-up and you can install the software clicking on the `Next` Button and accepting default parameters (note in which directory the program will be installed) until you have to click on the `Finish` button.
3. test Scratch
 * If you did not uncheck the options before clicking on `Finish`, you should see the program running and you coud reopen it using the desktop Scratch icon. Alternatively, you can open an explorer, go to the directory in which the program was installed and double click on the Scratch icon.
 * you should be able to move the little animal around

### Text Editor

1. If you are using a 64 bits version of Windows, install `atom`
 * use a file explorer (windows key + e) to open the directory in which you downloaded the installer file `atom-windows.zip`, for example the default `Downloads` directory.
 *
 * double-clicking on the installer `AtomSetup.exe`

2. If you are using a 32 bits version of Windows, install `Sublime Text`
*


### R and Rstudio

1. Installation of R
 * 1. Open a file explorer (windows key + e) and open the directory in which you downloaded the installer file `R-3.3.1-win.exe`.
 * Install R by double-clicking on the downloaded file and following the steps on the typical Windows installer pop-up window (usually you just have to clic on the `Next` button).  
 * Then install RStudio by double-clicking on the downloaded file. It should be straight forward.

2. Verification
 * Launch RStudio from the icon on your desktop
 * in the command window, type 'demo(graphics)'


### Git

0. Set up an account on Github.com
 * Open an internet browser and go to [http://github.com]
 * fill the requested fields with appropriate username, email, and password
 * click on the `Sign up for Github` button
1. Download the application
 * Go to [http://desktop.github.com] and click on the `Download GitHub Desktop` button.
2. Installation
 * It should start automatically, otherwise go to your `Downloads` folder and double click on the "GitHubSetup.exe" file

3. configuration: you should see a window that says "Welcome"
 * fill the username and password and click on `login`, then your email and click on `Continue`
 * skip the local repository search
 * now you can just quit the "Github Desktop" application

4. In case your Windows version is earlier than "Windows 7" (i.e. "XP", "Vista",...), get the installer from [https://github.com/git-for-windows/git/releases/tag/v2.5.1.windows.1], then ask for help during the installation party.

### Python

0. if you have trouble with the anaconda installation that we told you we cannot solve, here is a link to the Christophe Gohlke 64bits modules [http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame]

1. Downloads
 * If you have a 64 bits Windows, download the Windows 64-Bit Python 2.7 Graphical Installer `Anaconda2-4.1.1-Windows-x86_64.exe` from [this link](https://repo.continuum.io/archive/Anaconda2-4.1.1-Windows-x86_64.exe) of directly from https://www.continuum.io/downloads
 * if you have a 32 bit Windows XP, then download instead the Windows 32-Bit Python 2.7 Graphical Installer `Anaconda2-4.1.1-Windows-x86.exe` from [this link](https://repo.continuum.io/archive/Anaconda2-4.1.1-Windows-x86.exe) or directly from https://www.continuum.io/downloads

2. Installation of the Anaconda distribution

 * go to your `Downloads` folder and double click on the "Anaconda-X.X.X-Windows-" file
 * confirm that you want to run the file on the security warning pop-up window
 * on the Anaconda Setup Wizard, beware, you will have to change one option, so click `Next` on the opening panel
 * then 'Agree' with the licence agreement
 * verify that you Install for `Just Me (recommended)`, then click on `Next`
 * use default Destination folder and click on `Next`
 * check that both "Add Anaconda to my PATH" and "Register Anaconda as my default Python 2.7" are ckecked and click on `Install`
 * upon completion, click on 'Next', then `Finish`

 5. Test
 * click on the windows icon on the left bottom of your screen. For windows 8 early version users, use your search command to find the application using its name.
 * click on `All the programs` and then the `Anaconda (64-bit)` folder, what you are looking for is the `IPython (Py 2.7)` entry. Click there (and not the `IPython (Py 2.7) Notebook` nor the `IPython (Py 2.7) QTConsole`).
 * this launches a window that understands only commands in the python language
 * in just after the `$` sign, type each of those lines one by one followed by a stroke on the `enter` key

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

3. Configuration

 * click on the windows icon on the left bottom of your screen. For windows 8 early version users, use your search command to find the application using its name.
 * click on `All the programs` and then the `Anaconda folder`, then on `Anaconda Command Prompt`
 * this launches the anaconda terminal, where you have to type this text and then press on the `Enter` key:
    ```
    conda install conda
    ```
    You have to type it where a little rectangle is blinking (this is the "prompt"), after something that looks like `C:Users\your_name\AppData\Local\continuum\Anaconda>`
    You will see some text messages during the installation of some python modules, don't worry!
 * when you are asked `Procced ([y]/n)`, press on the `Enter` key (because yes is the default)
 * **WARNING** **if you have a 32bit Windows, stop the install process rigth now, do not install anything past this point!**
 * when you are back to the blinking little rectangle, type this text, then press the `Enter` key:
    ```
    conda install -c https://conda.binstar.org/krisvanneste pygame
    ```

 * When the installation of pygame is over, you can even type `exit` and press on `Enter` to close the window, how spooky!

4. Test

 * click on the windows icon on the left bottom of your screen. For windows 8 early version users, use your search command fo find the application using its name.
 * click on `All the programs` and then the `Anaconda folder`, then on `Ipython (Py 2.7) QTConsole`
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
    You should see a little window appear, change color and then disappear.
 * press the keys `ctrl+D` to quit the ipython console
 * click on the `Windows` icon (or just press the `Windows` key on your keyboard), then on `All the programs` and then the `Anaconda folder`, then on `Anaconda Command Prompt`
 * at the prompt, type the following text then press on `Enter`
     ```
     python Lib\site-packages\pygame\examples\chimp.py
     ```

     You should be able to play a silly game, including sound (make sure the sound is on, but not too loud).

__________________________________________________

## Mac OS

### Warming up
1. Know you system version, so you can chose which file to download
 * First go to the "apple" menu by clicking on the apple icon at the upper-left corner of the screen.
 * Select "About This Mac", and look at the Version number, the first two numbers are the major releases:

| 10.2 | 10.3 | 10.4 | 10.5 | 10.6 | 10.7 | 10.8 | 10.9 | 10.10 | 10.11 |
|------|------|------|------|------|------|------|------|-------|-------|
| Jaguar | Panther | Tiger | Leopard | Snow Leopard | Lion | Mountain Lion | Mavericks | Yosemite | El Capitan |
| 2002 | 2003 | 2005 | 2007 | 2009 | 2011 | 2012 | 2013 | 2014 | 2015 |

2. Some configuration
 * make sure you know the administrator password for your computer (password used to install new software) and that you are able to type it blind.
 * clic on the `Finder` icon on your dock then click on the `Finder` text next to the `Apple` logo on the top left corner of your screen to get the menus, then on `Preferences`, then on the `Side Bar` tab, check the first unchecked box under `DEVICES`. Now you can close the `Finder Preferences` window.
 * go to your `Application folder` and then to the `Utilities` subfolder, grab the `Terminal` icon and put it on the second place on your "Dock", right next to the `Finder` icon.

### Command Line Tools
 * open a terminal by clicking on the `Terminal` icon you just placed in the "Dock".
 * In this window copy and paste the following text then press on the `Enter` key (from now on this will be called **executing a command in the terminal**)
   ```
   xcode-select --install
   ```

 * This should make a window pop up to ask you if you want to install the "Command Line Tools", answer `Yes`, and wait until completion of the installation

### XQuartz

1. Download `XQuartz-2.7.9.dmg` using [this link](https://dl.bintray.com/xquartz/downloads/XQuartz-2.7.9.dmg) or from [https://www.xquartz.org/]

2. Installation
 * double click on `XQuartz-2.7.9.dmg` in your `Downloads` folder or wherever you downloaded it.
 * double click on the `XQuartz.pkg`
 * click on `Continue` and `Agree` until you can click on `Install`

### Git

0. Set up an account on Github.com
 * Open an internet browser and go to [http://github.com]
 * fill the requested fields with appropriate username, email, and password
 * click on the `Sign up for Github` button
1. Download the application
 * Go to [http://desktop.github.com] and click on the `Download GitHub Desktop` button.
2. Installation
 * Go to your `Downloads` folder
 * decompress the `.zip` archive if needed
 * double-click on the `GitHub Desktop` icon
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

 4. For old Mac OS versions, go to [http://sourceforge.net/projects/git-osx-installer/files/l]
* get the appropriate version installer
* install it as usual

 ### Atom

1. Download the Atom installer by clicking on the big red `Download For Mac` button on [http://atom.io]

2. Install as usual

3. Enjoy!


### Scratch
1. Download [MacScratch1.4.dmg](http://download.scratch.mit.edu/MacScratch1.4.dmg) from http://download.scratch.mit.edu/
2. then install as usual:
 * select your `Downloads` folder from the `Dock`
 * clic on the .dmg file to mount the virtual disk that wraps the application
 * drag and drop this application to your `Applications` folder in the pop-up window
 * eject the virtual disk
3. test Scratch
 * select your `Applications` folder from the `Dock`
 * clic on the `Scratch1.4` folder
 * then clic on the `Scratch.app` icon
 * the Scratch window should appear on your screen and you should be able to drag and move the little animal around

### R

1. Downloads

 * Go to [http://cran.rstudio.com/bin/macosx/] and download either the "R-3.2.2.pkg" or the "R-3.2.1-snowleopard.pkg" depending on the version of your OS (check About this mac on the apple menu on the top left of your screen if needed).

 * download [RStudio-0.99.473.dmg](http://download1.rstudio.org/RStudio-0.99.473.dmg) from https://www.rstudio.com/products/rstudio/download/ or an appropriate older version from [https://support.rstudio.com/hc/en-us/articles/206569407-Older-Versions-of-RStudio-Desktop]


2. Installation
 * In the Finder open the folder in which you downloaded the R package. Double-click on it and do as usual.
 * go to the download folder then double-click on "RStudio-X.XX.XXX.dmg". In the window that pops up, slide the RStudio icon into the Applications folder.

3. Verification
 * Launch RStudio from the icon on your desktop
 * in the command window, type 'demo(graphics)


### Python

1. Preparation
 * First go to the "apple" menu in the upper-left corner of the screen. Select "About This Mac", and check that your version of Mac OS X is 10.7 or higher (for example 10.9.5 or 10.7.2 are higher, but 10.6.8 is lower). **If not or if you are not sure, don't install anything, and come see us tomorrow morning.**
 * Alternatively, clic on the `Apple` icon again, then on "About This Mac" window, now click on "More info..." and in the window that opens up seek the "Processor Name" entry in the "Hardware Overview". If it says "PowerPC", "Intel Core Solo" or "Intel Core Duo", then **stop right there before doing anything else, because you will need to wait until the Tuesday install party to get a different version of Python.**  
 * alternatively, open a terminal and type the following text, then press on the `Enter` key
     ```
     sysctl hw.cpu64bit_capable
     ```
     The output tells you if your processor can get huge instruction sets

    |architecture| output | so what? |
    |------------|--------|----------|
    |   64 bits  |  1     | Carry on |
    |   32 bits  | 0      | Stop right now |

 * If and only if your mac pass these tests, you can carry on.

2. Download Anaconda
 * Download the Anaconda distribution installer [Mac OS X — 64-Bit Python 2.7 Graphical Installer](https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda-2.3.0-MacOSX-x86_64.pkg) from [http://continuum.io/downloads]

3. Install the Anaconda python distribution
 * go to your `Downloads` folder and double click on the file Anaconda-X.X.X-MacOSX-x86_64.pkg in order to start the installation.
 * click on `Continue` several times and `Agree` on licence terms until the installation is completed, if at some point you see the error "You cannot install Anaconda in this location", then just click on `Install for me only` and you should be able to continue.
 * when you see the message "The installation was successful", click on the `Close` button

4. Configuration
 * you should see a Launcher.app icon on your desktop, double-click on it to start the launcher.
 * answer as you like about sending informations to the Continuum company
 * wait whil the laucher checks which python applications are installed
 * verify that `ipython-notebook` and `ipython-qtconsole` are installed (their icon should be `Update | Lauch`), otherwise, click on `Install` buttons.
 * close the "Laucher" window

5. Test
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

0. **Warning** Now the Mac python install procedure starts to be tricky, if you don't feel confident with typing commands in a terminal, of if you'd like to sleep, stop rigth now, we will carry on tomorrow morning.  
Otherwise, stay up for some more fun with the terminal!

7. Install "Homebrew
 * in a terminal, copy paste or type this command:
     ```
     ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
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

8. Install pygame dependencies
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
     conda install -c http://conda.binstar.org/quasiben pygame
     ```
 * when you are asked `Procced ([y]/n)`, press on the `Enter` key (because yes is the default
 * wait

11. Check the installation
 * in a terminal, type
     ```
     ipython qtconsole
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
 * press the keys `ctrl+D` to quit the ipython console
 * to further check the installation, in a Terminal window, type:
    ```
    python ~/anaconda/lib/python2.7/site-packages/pygame/examples/chimp.py
    ```
    You should be able to play a silly game, including sound (make sure the sound is on, but not too loud).

__________________________________________________

## Linux debian based

### Python

You must be connected to the Internet!

To download and install Python, as well as various libraries and documentation, copy paste the following line in a terminal and press 'Enter':

```
sudo apt-get install python2.7  python-numpy python-scipy python-matplotlib python-pandas ipython ipython-notebook python2.7-doc python2.7-examples python-numpy-doc python-matplotlib-doc ipython-doc python-pygame
```

2. Check the installation
 * in a terminal, type `ipython` in order to lauch a ipython interpreter
 * in the ipython shell, type each of those lines one by one followed by enter

```python
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import stats
    x=np.arange(-5,5,.1)
    y=stats.norm.pdf(x)
    plt.plot(x,y)
    plt.show()
```

 * exit the ipython shell by typing `quit()` or the keyboard shortcut `ctrl + D`

 * then you are back to the terminal shell where you can install pygame


3. If you want a look a the documentation you installed, use your favorite browser

 ```
 iceweasel /usr/share/doc/python2.7-doc/html/index.html
 ```

 and

 ```
 iceweasel /usr/share/doc/python-pygame/index.hml
 ```


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

You should see a new window, where you should be able to grab and move the little mascot.


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
    Description :   Debian GNU/Linux 8.2 (jessie)
    Release:        8.2
    Codename:       jessie
```

 * add the appropriate repository to your `/etc/apt/sources.list`

```
sudo sh -c 'echo deb http://cran.univ-paris1.fr/bin/linux/debian jessie-cran3/ >> /etc/apt/sources.list'
```

For Ubuntu, you migh have to leave out the -cran3 after the version codename

```
    sudo sh -c 'echo deb http://cran.univ-paris1.fr/bin/linux/ubuntu vivid/ >> /etc/apt/sources.list'
```


 * update your repository list

```
sudo apt-get update
```

* go to [http://www.rstudio.com/products/rstudio/download/] and download the appropriate `.deb` installer for Debian/Ubuntu. If your system is not that recent, go to [https://support.rstudio.com/hc/en-us/articles/206569407-Older-Versions-of-RStudio-Desktop] to find the appropriate installer file.


1. Installation
 * R

```
sudo apt-get install r-base r-base-core r-base-html
```

 * and, for Rstudio, replacing the XX by the version numbers

```
    sudo apt-get install libjpeg62
    sudo dpkg -i rstudio-X.XX.XXX-amd64.deb
```

3. Verification
 * type `rstudio` in a console to lauch the R interpreter
 * type 'demo(graphics)' and press on 'Enter' to see the graphs.

### Atom

```
sudo apt-get install atom
```

 But if you are using linux, you might already be using a decent text editor and thus won't need Atom.
