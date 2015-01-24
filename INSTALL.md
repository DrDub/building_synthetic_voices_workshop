Installation instructions
=========================

Download:

* Festival 2.4 (Dec 2014):

http://www.cstr.ed.ac.uk/projects/festival/download.html
http://festvox.org/packed/festival/2.4/festival-2.4-release.tar.gz

* Edinburgh Speech Tools 2.4:

http://festvox.org/packed/festival/2.4/speech_tools-2.4-release.tar.gz

* FestVox 2.7 (Dec. 2014):

http://festvox.org/festvox-2.7/festvox-2.7.0-release.tar.gz

* Wavesurfer 1.8.8 (Oct 2010), only for Mac OS X:

https://sourceforge.net/projects/wavesurfer/files/wavesurfer/1.8.8p4/



Debian and Debian derivatives
-----------------------------

Install dependencies and helpful programs:

  sudo apt-get install festival festival-dev festlex-cmu sox audacity wavesurfer
  sudo apt-get build-dep festival

Mac OS X
--------

You need to have to have [Homebrew](brew.sh) installed.

Install the dependecies

  brew install sox


Common Instructions
-------------------

After having installed the dependencies, create a folder
$HOME/workshop and download the files above

  mkdir $HOME/workshop
  cd $HOME/workshop
  wget http://festvox.org/packed/festival/2.4/festival-2.4-release.tar.gz
  wget http://festvox.org/packed/festival/2.4/speech_tools-2.4-release.tar.gz
  wget http://festvox.org/festvox-2.7/festvox-2.7.0-release.tar.gz

go to $HOME/workshop and extract the files:

  cd $HOME/workshop
  tar -zxf festival-2.4-release.tar.gz
  tar -zxf speech_tools-2.4-release.tar.gz
  tar -zxf festvox-2.7.0-release.tar.gz

build the Edinburgh Speech Tools:

  cd $HOME/workshop/speech_tools
  ./configure
  make
  export ESTDIR=`pwd`

build Festival:

  cd $HOME/workshop/festival
  ./configure
  make
  export FESTIVAL_HOME=`pwd`

buid FestVox

  cd $HOME/workshop/festvox
  ./configure
  make
  export FESTVOXDIR=`pwd`


Notes:

* We use the system festival even though it is a different version
  from the one compiled from source, that seems to work fine given
  this workshop and the version numbers.

* Compiling Festival from source might not be necessary.





  