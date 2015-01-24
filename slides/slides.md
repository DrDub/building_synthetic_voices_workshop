Building Synthetic Voices
=========================

Workshop at Les Laboratoires Foulab

January 24th, 2015

Pablo Duboue, PhD

---

* This workshop
* Foulab
* Pablo

---

This workshop
-------------

Introduction to a complex topic.

Learn something you can play and experiment.

You will need to be patient and feel comfortable with partial understanding.

---

Foulab
------

A place to break things.

Learn new things, by doing!

Open House night, Tuesday nights after 8PM: a sanctuary for the
technical counter culture in Montreal.

---

Pablo
-----

I work on Natural Language Processing / Machine Learning.

Not an speech expert per se, but interested in learning more.

My personal site: [http://duboue.net](http://duboue.net)

My 2014 class (in Spanish): [http://aprendizajengrande.net](http://aprendizajengrande.net)

---

TTS: simulation vs. emulation
-----------------------------

* Simulation: generate a sound wave by simulating air going through
  the different parts of the human speech apparatus. More language
  independent.

* Emulation: generate a sound wave by other means (concatenating and
  adapting examples from a speech database) so that humans will
  recognize it as speech. More language dependent.

To know more: [BSV Chapter 1, "History"](http://festvox.org/bsv/c59.html#AEN61)

---

Concepts of linguists
---------------------

* Part-of-speech
* Prosody
* Vowels, consonants, types of

---

Parts of speech
----------------

A word in context belongs to different classes of words depending on
its function in the sentence.

For examine the word "flies"  in "time flies like an arrow" is a verb. 

Identifying the correct POS for a word is important for text-to-speech
because different classes of words are stressed differently. Moreover
some words are written the same and pronounced differently given their
POS (e.g., "read:)

---

Prosody
-------

Prosody is the sub-field of linguistics that studies
intonation. Natural stress is the key for non-monotonous speech
synthesis.

A key concept here is new versus old information. New information
tends to be further stressed.


---

Vowels, consonants, types of
----------------------------

* http://en.m.wikipedia.org/wiki/IPA_vowel_chart_with_audio
* http://en.m.wikipedia.org/wiki/Help:IPA

---

Festival project, tools
-----------------------

![Dr Black](http://www.cs.cmu.edu/~awb/images/awb.jpg)

a C engine with an embedded scheme API.

No knowledge of C is needed for more user-facing interaction.

Python?

---

The utterance data structure
----------------------------

<pre>
$ Festival
festival> (set! u1 (utt.synth (eval (list 'Utterance 'Text "hola"))))
#<Utterance 0x7f0810897f30>
festival> (utt.relationnames u1)
(Token
 Word
 Phrase
 Syllable
 Segment
 SylStructure
 IntEvent
 Intonation
 Target
 Unit
 SourceCoef
 f0
 TargetCoef
 US_map
 Wave)
</pre>

---

Word level
----------

<pre>
festival> (item.features (car (utt.relation.items u1 'Word)))
((id "_2")
 (name "hola")
 (pos_index 8)
 (pos_index_score 0)
 (pos "nnp")
 (phr_pos "n")
 (pbreak_index 0)
 (pbreak_index_score 0)
 (pbreak "B")
 (blevel 3))
</pre>

---

Syllable level
--------------

<pre>
festival> (item.features (car (utt.relation.items u1 'Syllable)))
((id "_4") (name "syl") (stress 1))
</pre>

---

Target level
------------

<pre>
festival> (item.features (car (utt.relation.items u1 'Target)))           
((id "_5")
 (name "hh")
 (dur_factor 0.45713699)
 (end 0.30117983)
 (source_end 0.177259))
</pre>

---

Unit level (diphone)
--------------------

<pre>
festival> (item.features (car (utt.relation.items u1 'Unit)))  
((id "_19")
 (name "pau-hh")
 (sig "[Val wave]")
 (coefs "[Val track]")
 (middle_frame 7)
 (end 0.143197)
 (num_frames 14))
</pre>

---

Diphone synthesis
-----------------

IDEA: the boundary between syllables is very varied, but the middle is
not. Record these boundaries (half-syllables) and assemble continuous
speech from them.

To know more: [BSV Chapter 11, "Diphone databases"](http://festvox.org/bsv/c2265.html)

---

Unit selection synthesis
------------------------

IDEA: extend the concept of diphones to larger units. Select the unit
on-the-fly using information from the context where the unit is being
spoken.

To know more: [BSV Chapter 12, "Diphone databases"](http://festvox.org/bsv/c2645.html)

---

Where to use diphone synthesis
------------------------------

* Festival
* FreeTTS (Java)
* eflite
* PD Speech patch

---

Where to go from here
---------------------

* Spanish/French
* Finding prompts automatically
* Millenium prompts
* Chess

<i>
Whites played by Kramnik,V. Blacks played by Anand,V. ECO information
available. First move, white moves pawn to d4. Black moves pawn to
d5. Second move, white moves pawn to c4. Good move. Black moves pawn
to c6. Potential mistake. Third move, white moves knight to
c3. Brilliant move. Black moves knight to f6. Very bad move. Fourth
move, white moves pawn in c to d5 and it captures a piece. The
Exchange Slav, the sure way to play with zero losing chances so an
ideal choice for game one. Continuing the fourth move, black moves
pawn in c to d5 and it captures a piece. Potentially inaccurate
move. Fifth move, white moves bishop to f4. Black moves knight to c6.
</i>
