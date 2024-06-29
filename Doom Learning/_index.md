---
weight: 1
title: Doom Learning
bookHidden: true
---

# Doom Learning

## VizDoom
<a href="http://vizdoom.cs.put.edu.pl">ViZDoom</a> <a href="#wydmuch2018vizdoom">[6]</a> allows developing AI bots that play DOOM using the visual information (the screen buffer). It is primarily intended for research in machine visual learning, and deep reinforcement learning, in particular. For this section we specifically focus on the portions of the codebase (the environment) that are relevant in order to understand it's relationship with ML models. The full repo is available on <a href="https://github.com/mwydmuch/ViZDoom">GitHub</a>.

<img src="/~bebeal/Doom/doomscenes.gif" class="center"/>

### State
Calling `getState()` will return a `GameState` object which has the following fields:
- `int` **number**: 
- `int` **tic**
- `numpy.double[]` **game\_variables**
- `numpy.uint8[]` **screen\_buffer**
- `numpy.uint8[]` **depth\_buffer**
- `numpy.uint8[]` **labels\_buffer**
- `numpy.uint8[]` **automap\_buffer**
- `list` **labels**

### Action

### Relevant Options

## Doom AI Competition
From 2016-2018, a Visual Doom AI Competition (VDAIC) was held annually at the IEEE Computational Intelligence and Games (CiG) conference. We briefly analyzed and referenced a few of the more competitive models that performed in the competition throughout the three years.

### F1
The F1 model <a href="#Wu2017F1">[5]</a> by the Facebook AI Research team won the 2016 limited death match mode by a large margin, scoring 35\% higher than the second
place model. F1 totalled 559 frags, a 1.35 K/D ratio, 597 kills, 38 suicides and, 413 deaths. It was trained on a variant of the A3C algorithm <a href="#mnih2016asynchronous">[4]</a> (specifically, BatchA3C) with curriculum learning <a href="#bengio2009curriculum">[3]</a>. 

#### Architecture


### IntelAct
#### Architecture

### Marvin/Marv2in
#### Architecture

### Arnold2/Arnold4
#### Architecture

### TSAIL
#### Architecture

## Our Model

### State representation

### Action space

### Crafting the Reward Function

### Optimizations

### Framework

### Training

### Evaluation and Results



## References
<table>

<tr valign="top">
<td align="right" class="bibtexnumber">
[<a name="VizDoomSite">1</a>]
</td>
<td class="bibtexitem">
Vizdoom.
 <a href="http://vizdoom.cs.put.edu.pl">http://vizdoom.cs.put.edu.pl</a>.

</td>
</tr>


<tr valign="top">
<td align="right" class="bibtexnumber">
[<a name="VizDoomRepo">2</a>]
</td>
<td class="bibtexitem">
Vizdoom repo.
 <a href="https://github.com/mwydmuch/ViZDoom">https://github.com/mwydmuch/ViZDoom</a>.

</td>
</tr>


<tr valign="top">
<td align="right" class="bibtexnumber">
[<a name="bengio2009curriculum">3</a>]
</td>
<td class="bibtexitem">
Yoshua Bengio, J&eacute;r&ocirc;me Louradour, Ronan Collobert, and Jason Weston.
 Curriculum learning.
 ICML '09, New York, NY, USA, 2009. Association for Computing
  Machinery.
<a href="http://dx.doi.org/10.1145/1553374.1553380">DOI</a>&nbsp;

</td>
</tr>


<tr valign="top">
<td align="right" class="bibtexnumber">
[<a name="mnih2016asynchronous">4</a>]
</td>
<td class="bibtexitem">
Volodymyr Mnih, Adrià&nbsp;Puigdomènech Badia, Mehdi Mirza, Alex Graves,
  Timothy&nbsp;P. Lillicrap, Tim Harley, David Silver, and Koray Kavukcuoglu.
 Asynchronous methods for deep reinforcement learning, 2016.
<a href="http://arxiv.org/abs/1602.01783">arXiv</a>&nbsp;]

</td>
</tr>


<tr valign="top">
<td align="right" class="bibtexnumber">
[<a name="Wu2017F1">5</a>]
</td>
<td class="bibtexitem">
Yuxin Wu and Yuandong Tian.
 Training agent for first-person shooter game with actor-critic
  curriculum learning.
 In <em>ICLR</em>, 2017.

</td>
</tr>


<tr valign="top">
<td align="right" class="bibtexnumber">
[<a name="wydmuch2018vizdoom">6</a>]
</td>
<td class="bibtexitem">
Marek Wydmuch, Michal Kempka, and Wojciech Ja&#x15b;kowski.
 Vizdoom competitions: Playing doom from pixels.
 <em>IEEE Transactions on Games</em>, 2018.

</td>
</tr>
</table>