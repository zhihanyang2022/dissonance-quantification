

# Dissonance in *Threnody*

​															Zhihan Yang

### Penderecki and *Threnody*

Krzysztof Penderecki, born on 23 November 1933, is a Polish composer and conductor. He is an avant-garde in Polish music known for challenging old beliefs in meaning and composition of comtemporary music and for exploiting strings in unconventional ways. The innovations he brought into music notation, time perception and instrument techniques earned him reputation early on in his career. Some of his well-known works are *Anaklasis*, *Threnody to the Victims of Hiroshima*, *St. Luke Passion* *Symphony No. 3* and *Polish Requiem*.

*Threnody to the Victims of Hiroshima* was composed in 1960. The piece was originally named 8'37'' for its duration. Penderecki later dedicated the piece to victims of Hiroshima after feeling a strong emotional response following a performance of the piece. "[This] threnody express[es] [Penderecki's] deep belief that the sacrifice of Hiroshima will never be forgotten and lost, and Hiroshima will become a symbol of brotherhood between people of good will."

### Quarter Tones, Tone Clusters and Their Notations

In western music, a tone cluster commonly refers to a set of at least three adjacent tones of a 12-tone scale played simultaneously, with each adjacent pair of tones parted by a semitone. This definition of semitone is rooted in the way by which the pitch spectrum is divided:

1. Let the pitch spectrum be denoted as $S$, which is all the real numbers.
2. A pitch group $X=\{x, 2x, \cdots, 2^nx\}$  are selected from $S$ with $n\geq2$.
3. A subset of $S$, $x$ to $2^nx$ (inclusive), is binned into intervals with elements of $X$ as bin edges. The resulting intervals are each called an octave.
4. Between the pair of bin edges of each octave, define eleven more bin edges such that the second bin edge equals to the first bin edge multipled by $2^{\frac{1}{12}}$, the third bin edge equals to the second bin edge multiplied by $2^{\frac{1}{12}}$ and so on. The resulting smaller intervals are each called a semitone.

A quarter-tone is "a interval half the size of a semitone" [4]. Using quarter-tones, the 12-tone scales can be elaborated into 24-tone scales. As a result, a tone cluster may also be a set of at least three adjacenent tones of a 24-tone scale played simultaneously, with each adjacent pair of tones parted by a quarter-tone. The notation for quarter-tones in *Threnody* are shown below.

![Screen Shot 2019-02-13 at 8.34.04 AM](/Users/yangzhihan/Desktop/Screen Shot 2019-02-13 at 8.34.04 AM.png)

### Between Rehearsal Number 16 and 19

By mathematical treatment, one can conveniently spot the meta-parameters and  analyze the consequences of changing them. Between rehearsal no. 16 and no. 18 of the *Threnody*, there are eight tone clusters, all using quarter-tones as intervals. Instead of having twelve intervals or eleven bin edges between the pair of bin edges of each octave, we must now have twenty four intervals or twenty three intervals. As a result, the difference in frequency between adjacent bin edges halved - pitches are more densely packed. Therefore, a natural question would be: does the use of quarter-tones, which essentially leads to more densily packed frequency components, promote the irritating sensation?

Imagine if Penderecki used only semitones in the first tone cluster (Fig. 1) between rehearsal number 16 and 18. This is shown in Table 1. As no semitones and integer multiples of semitones cannot be derived from larger semitones, (1) the average interval and pitch differences between tones increases, and (2) the total number of possible interval and pitch differences drastically decreases (Fig. 2 and Fig. 3). Since the frequency of beat, $f_{\textrm{beat}}​$, is equal to the difference in frequency between two tones,
$$
f_{\textrm{beat}}=|f_1-f_2|,
$$
and "roughness [...] increases to a maximum for 33 beats" (Helmholtz, 1863), it is clear from (1) and (2) that the first tone cluster has a higher roughness with quarter-tone. Unfortunately, the differences in frequency in overtones were not analyzed due to combinatory explosion.

![](/Users/yangzhihan/Desktop/threnody-for-the-victims-of-hiroshima-1960-detail-from-score-06 2.jpg)

​							**Figure 1.** The first tone cluster between rehearsal no. 16 and 18 (refer to Appendix A). 

| Tones of 1st Tone Cluster (with quarter-tones) | f / Hz (3 s.f.) | Tone of 1st Tone Cluster (quarter-tones removed) | f / Hz (3 s.f.) |
| ---------------------------------------------- | :-------------: | ------------------------------------------------ | --------------- |
| A + semitone                                   |       466       | A + semitone                                     | 466             |
| A + three quarter-tones                        |       480       |                                                  |                 |
| B                                              |       494       | B                                                | 494             |
| B + one quarter-tones                          |       508       |                                                  |                 |
| C                                              |       523       | C                                                | 523             |
| C + one quarter-tones                          |       539       |                                                  |                 |
| C + semitone                                   |       554       | C + semitone                                     | 554             |
| C + three quarter-tones                        |       571       |                                                  |                 |
| D                                              |       587       | D                                                | 587             |
| D + one quarter-tones                          |       605       |                                                  |                 |
| D + semitone                                   |       622       | D + semitone                                     | 622             |
| D + three quarter-tones                        |       640       |                                                  |                 |

​		**Table 1. ** Tones of the first tone cluster with quarter-tones and tones of the first tone cluster with quarter-tones removed.

![](/Users/yangzhihan/Desktop/Histogram of Frequency Differences with Quarter-Tones.png)

​								**Figure 2. ** Histogram of frequency differences with quarter-tones.

![](/Users/yangzhihan/Desktop/Histogram of Frequency Differences with No Quarter-Tones.png)

​								**Figure 3. ** Histogram of frequency differences with no quarter-tones.

In order to quantify the roughness between rehearsal number 16 and 19, let us first break things down a little bit. Let us analyze Page 10 and Page 11 separately as this would be good for comparision for the next section. On Page 10, there are eight distinct tone clusters, labelled by Arabic numbers in Appendix A. They fade in and fade out at different times, and sustain for different lengths. As we progress in time starting from rehearsal number 16, we get 7 different temporal combinations of the tone clusters, labelled by Roman numerals in Appendix A. Each tone cluster is a collection of frequencies played concurrently.

| Tone Cluster |                         Frequencies                          |
| :----------: | :----------------------------------------------------------: |
|      1       | 466.0, 480.0, 494.0, 508.0, 523.0, 539.0, 554.0, 571.0, 587.0, 605.0, 622.0, 640.0 |
|      2       | 587.0, 605.0, 622.0, 640.0, 659.0, 679.0, 698.0, 719.0, 740.0, 762.0, 784.0, 807.0 |
|      3       | 554.0, 571.0, 587.0, 605.0, 622.0, 640.0, 659.0, 679.0, 698.0, 719.0, 740.0, 762.0 |
|      4       | 784.0, 807.0, 831.0, 855.0, 880, 906.0, 932.0, 960.0, 988.0, 1017.0, 1047.0, 1077.0 |
|      5       | 415.0, 427.0, 440, 453.0, 466.0, 480.0, 494.0, 508.0, 523.0, 539.0 |
|      6       | 880, 906.0, 932.0, 960.0, 988.0, 1017.0, 1047.0, 1077.0, 1109.0, 1141.0 |
|      7       | 330.0, 339.0, 349.0, 359.0, 370.0, 381.0, 392.0, 403.0, 415.0, 427.0 |
|      8       |     392.0, 403.0, 415.0, 427.0, 440, 453.0, 466.0, 480.0     |

Since each section is made up of one or several different tone clusters:

| Section | Made up of Tone Cluster(s) |
| :-----: | :------------------------: |
|    I    |             5              |
|   II    |            3, 5            |
|   III   |         1, 3, 5, 8         |
|   IV    |         1, 3, 6, 8         |
|    V    |       1, 3, 6, 7, 8        |
|   VI    |       2, 3, 6, 7, 8        |
|   VII   |       2, 4, 6, 7, 8        |

We can also think of each section as a bigger collection of frequencies. For each section, we compute all the possible frequency differences (which equal to the beat frequencies) between each pair of frequencies in its collection. Then, a scoring function can be applied on each frequency difference. "In order to construct [the scoring function, Helmholtz was] forced to assume a somewhat arbitrary law for the dependence upon the number beats. [Helmholtz] chose [...] the simplest mathematical formula which would shew that the roughness vanishes when there are no beats, increases to a maximum for 33 beats, and then diminishes as the number of beats increases." Therefore, it is reasonable to construct the following scoring function,
$$
\textrm{score}(x)=
\left\{\begin{matrix}
y=\frac{1}{33}x, \: \textrm{if} \: x \leq 33 \\ 
y=-\frac{1}{132-33}x+\frac{4}{3}, \: \textrm{if} \: x > 33,
\end{matrix}\right.
$$
where $y$ denoted roughness and $x$ denotes beat frequency. The function is visualized in Fig. 4.

![Screen Shot 2019-02-13 at 7.40.35 AM](/Users/yangzhihan/Desktop/Screen Shot 2019-02-13 at 7.40.35 AM.png)​		**Figure 4.** Visualization of $\textrm{score}(x)$. The function inputs beat frequency (x-axis) and outputs roughness (y-axis) on a 0-to-1 scale. The function outputs zero when the input is zero or 132 Hz; the function outputs one when the input is 33 Hz.

The distribution of roughness of intervals for each section are visualized using histograms in Appendix B. It is clear that section 3 to 7 had many intervals that qualify as high roughness, that is, of score 0.9 to 1.0.

A sound is translated into liquid vibrations in the cochlear before any perception happens. When extended, the cochlear is a cylindrical tube with descending cross-sectional area, so that different parts of the cochlear have different natural frequencies and resonate with different frequencies within the sound. However, when two sounds of very similar frequencies enter the cochlear fluid, two very close regions of the cochlear resonate, leading to symathetic vibration between the two regions and causing beating. Fig. 5 shows the symapthetic vibrations of two simple waves of slightly different frequencies. Notice that the intensity of the waveform beats, that is, it increases and decreasings on regularly. Such beating causes auditory neurons to switch quickly between firing and resting, which makes the listener very uncomfortable. 

![Screen Shot 2019-02-13 at 8.52.21 AM](/Users/yangzhihan/Desktop/Screen Shot 2019-02-13 at 8.52.21 AM.png)

​			**Figure 5.** The waveform of the sympathetic vibrations of two simple waves of slightly different frequencies.

An interesting observation is that, apart from high roughness intervals, there are also plenty of low roughness ones, as shown by histograms in Appendix B. However, just like the most noticeable things on a white shirt are ink spots, the discomfort brought by high roughness and dissonance captures all our attention. 

Since the tone clusters on page 11 are also tones separated by quarter-tones, our ears react to them in similar manner. 

### Comparison of timber

Instead of starting each tone cluster by starting all the tones at once, Pendereck did something different on Page 11. He started each tone cluster one tone at a time with juxtaposing pitches. Before the clusters are fully formed, the pitch components over the pitch spectrum is much more spreadout compared to that of Page 10, resulting in a very different timbre. After the tone clusters matured, the timbre of page 10 and 11 are almost identical.

### Conclusion

*Threnody* is the landmark of dissonance. From Appendix B, we can see that the number of high roughness intervals (with score from 0.5 to 1.0)  (which is essentially dissonance) is almost equal or higher than the number of low roughness intervals (with score from 0.0 to 0.4) (which is essentially consonance). I have never music that are more dissonant than *Threnody*.

### References

1. Thomas, A.  (2001, January 01). Penderecki, Krzysztof. *Grove Music Online.* Ed.   Retrieved 13 Feb. 2019, from http://www.oxfordmusiconline.com/grovemusic/view/10.1093/gmo/9781561592630.001.0001/omo-9781561592630-e-0000021246.
2. Krzysztof Penderecki. (2019, January 23). Retrieved from https://en.wikipedia.org/wiki/Krzysztof_Penderecki

2. 1992 – Krzysztof Penderecki. (2015, August 31). Retrieved from http://grawemeyer.org/1992-krzysztof-penderecki/

3. Mazes, Notes & Dali: The Extraordinary Life of Krzysztof Penderecki. (2013, November 22). Retrieved from https://culture.pl/en/article/notes-on-penderecki
4. Rushton, J.  (2001, January 01). Quarter-tone. *Grove Music Online.* Ed.   Retrieved 13 Feb. 2019, from http://www.oxfordmusiconline.com/grovemusic/view/10.1093/gmo/9781561592630.001.0001/omo-9781561592630-e-0000022645.
5. Helmholtz. On the Sensations of Tone.
6. Huron, D. Voice Leading: The Science Behind a Musical Art

### Appendix A

The tone clusters are denoted by Arabic numbers; the sections are denoted by Roman numerals.

![168](/Users/yangzhihan/Desktop/168.png)





### Appendix B

![img1](/Users/yangzhihan/Desktop/img1.png)

![img2](/Users/yangzhihan/Desktop/img2.png)

![img3](/Users/yangzhihan/Desktop/img3.png)

![img4](/Users/yangzhihan/Desktop/img4.png)

![img5](/Users/yangzhihan/Desktop/img5.png)

![img6](/Users/yangzhihan/Desktop/img6.png)

![img7](/Users/yangzhihan/Desktop/img7.png)

















