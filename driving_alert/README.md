Bicycle Driving Alerts Example Domain
=====================================

A limited domain in with bicycle safety alerts [1].


Set up
------

Go to the workshop folder and create a folder to contain the voice:

  mkdir $HOME/workshop/foulab_driving_me

You can replace "foulab" for any other organization that better
describes you or use "net" for a generic one. It is better if you
replace "me" with your initials. Now use the FestVox limited domain
bootstrapping script:

  cd $HOME/workshop/foulab_driving_me
  $FESTVOXDIR/src/ldom/setup_ldom foulab driving me

if you are using a different organization change the foulab here and
change your initials, too.

The bootstrapping script will complain it doesn't know about driving
alerts so you need to provide the data file. Copy the file
driving.data to the etc/ folder. This file contains the prompts.


Generate prompts
----------------

The next step is to generate the prompts using an existing voice:

  cd $HOME/workshop/foulab_driving_me
  festival -b festvox/build_ldom.scm '(build_prompts "etc/driving.data")'

This step will produce a set of synthesized wave files in
$HOME/workshop/foulab_driving_me/prompt-wav/

Now we're ready to record the prompts. However, the default script
uses /dev/dsp for recording, which won't work in most modern operating
systems. Edit $HOME/workshop/foulab_driving_me/bin/prompt_them and
look for the line USE_SOX=0 and change it to USE_SOX=1

Record the prompts by doing

  cd $HOME/workshop/foulab_driving_me
  bin/prompt_them etc/driving.data

if you record something wrong press CTRL+C and restart from a given
prompt number, say prompt number 5:
  
  cd $HOME/workshop/foulab_driving_me
  bin/prompt_them etc/driving.data 5

it is good to record just one prompt and then listen to the wave file
in wav/driving0001.wav to make sure it is being recorded correctly and
with an acceptable level of noise.


Aligning the prompts
--------------------

The next step is to align your recorded voice to the original text:

  cd $HOME/workshop/foulab_driving_me
  bin/make_labs prompt-wav/*.wav

this will populate the folder $HOME/workshop/foulab_driving_me/lab.
These files can be edited and visualized with wavesurfer (see
[DEBUG](../DEBUG.md)), to correct some blatant mistakes.

From these alignments the full utterance structure is built by copying
the information from the synthesized speech into your timing data:

  cd $HOME/workshop/foulab_driving_me
  festival -b festvox/build_ldom.scm '(build_utts "etc/driving.data")'


Pitchmarks
----------

We now need to extract pitchmarks from the wave files. This process is
quite error prone and depends on some frequency parameters inside the
script. You might need to tune the parameters before obtaining
acceptable output (see Chapter 4 from BSV for details). What is for
sure is that you will need to use a different set of parameters if you
are recording a female voice.  The parameters are in
bin/make_pm_wave. If you are recording a female voice change
FEMALE_ARGS to PM_ARGS and delete the next line that sets PM_ARGS.

  cd $HOME/workshop/foulab_driving_me
  bin/make_pm_wave wav/*.wav

this populates the pm/ folder. If it complains the file
etc/txt.done.data is missing copy etc/driving.data into
etc/txt.done.data.

These post processing scripts are not mandatory but help:

  cd $HOME/workshop/foulab_driving_me
  bin/make_pm_fix pm/*.pm
  bin/simple_powernormalize wav/*.wav

Finally, we can obtain the mcep data:

  cd $HOME/workshop/foulab_driving_me
  bin/make_mcep wav/*.wav


NOTE: To visualize them and edit them, you need to generate pm_lab files

  cd $HOME/workshop/foulab_driving_me
  bin/make_pmlab_pm pm/*.pm

if you edit the files in pm_lab you will need to transfer back the information with

  cd $HOME/workshop/foulab_driving_me
  bin/make_pm_pmlab pm_lab/*.lab


Building the voice
------------------

The last step is to generate the actual voice:

  cd $HOME/workshop/foulab_driving_me
  festival -b festvox/build_ldom.scm '(build_clunits "etc/driving.data")'

To use the voice:

  cd $HOME/workshop/foulab_driving_me
  festival festvox/foulab_driving_me_ldom.scm '(voice_foulab_driving_me_ldom)'

This will bring the festival prompt

  (SayText "In 30 meters, you will encounter a car that might not be able to see you.")
  (SayText "In hour meters, you will intersection a pedestrian that might not be able to bicycle you.")





[1] Such a system is beyond the state of the art in terms of sensor
processing technology.