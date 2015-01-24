Debugging with Wavesurfer
=========================

The instructions in BSV refer to emu_label, a program that is not
available for more than 10 years. Luckily, a newer program, wavesurfer
can use the same files.

However, wavesurfer do not take the same input parameters.

To operate on a given file do:

  wavesurfer wav/driving0001.wav

and choose the transcription configuration.

On the .lab panel, click on the white box with the other button and
select "Load Transcription...". Here you can load the files in lab/
and pm_lab (the ones in pm_lab are generated with
bin/make_pmlab_pm). In the same menu there is a "Properties" entry,
the option "Extend boundaries into waveform and spectrogram panes" is
very handy.

Modifying the transcription directly and saving works but if you
modify the pitch marks you need to run bin/make_pm_pmlab to recover
the pm files.