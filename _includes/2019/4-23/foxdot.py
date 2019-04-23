Clock.bpm = 60
Scale.default.set("major")

# -- Pitches for each phrase
# 1
pphrase1 = P[0, 2, 3, 3.5, 4]#.shuffle().shufflets(3)
# 2
pphrase2 = P[7, 5.5, 5, 4,  5]#.invert()
# 3
pphrase3 = P[7, 5.5, 7, 7, 7, 7, 8]
# Ending
pphrase4 = P[7, 5.5, 5, 4, 5, 0, 1, 1.5, 1, 0]

# -- Durations for each phrase
# 1
rphrase1 = P[1, 2/3, 1/3, 1/2, 3/2 ]#.shuffle()
# 2
rphrase2 = P[1, 2/3, 1/3, 1/2, 3/2]#.shuffle()
# 3
rphrase3 = P[1/3, 2/3, 3/2, 2/3, 1, 2/3, 3/2 + 2/3 +1 ]#.shuffle()
# Ending
rphrase4 = P[1, 2/3, 1/3, 2/3, 1/3, 2/3, 1/3, 1, 2/3, 1/3 + 2]

# -- Melody
# By intervals, 0 is C, 2 is E, so on ..
# plucked guitar
s1 >> pluck(    # Pitches
                pphrase1  | pphrase2  | pphrase3 | pphrase4,
                # Durations
                dur = [rphrase1 | rphrase2 | rphrase3 | rphrase4],
                amp = 0.75, # Amplitude
                lpf = 700,  # low and high pass filters: cuts a frequency range
                hpf = 300 ,  #     out for pluck to be heard & not compete
            )

help(Pattern())

# plucked double bass
db >> dbass(    # Pitches
                pphrase1  | pphrase2  | pphrase3  | pphrase4,
                # Durations
                dur = rphrase1 | rphrase2 | rphrase3 | rphrase4,
                amp = 0.75 , # Amplitude
                lpf= 300    #double bass is now alone in freq. range
              )

# brass section
sw >> swell(    # Pitches
                pphrase1  | pphrase2  | pphrase3  | pphrase4,
                # Durations
                dur = rphrase1 | rphrase2 | rphrase3 | rphrase4,
                amp = 0.75 #, # Amplitude
              )

# no rests! not sure how to add them, so just extended notes too long.

# -- Add Drums!
# Made from drum samples

dr >> play("xxxxxxxx        xxxxxxxx",
            bpm = 30)


# -- Halt all insruments
# s1.stop()
#
# db.stop()
#
# sw.stop()
#
# dr.stop()



# -- Thoughts on instrument choices that sound decent
# - To see all, use command
# -     print(SynthDef)
# --------------------------------
# scatter - soso, not accurate
# charm
# bell
# gong
# viola
# klank - for new agey reverb/ reflections/echoes
# feel - like klank, less reverb
# glass - new agey, can't even hear melody, just have fragments'
# soft - varies loudness and messes up accuracy of rhythms and notes, like scatter
# quin - sounds like harmonica or reed organ or bad accordian, or melodica
# spark - new agey but accurate, almost like a pluck followed by brass section
# blip - accurate, almost like xylophone
# ripple - like accordian
# creep - gets louder as note goes on... otherwise really annoying
# orient - modeled off of middle eastern harp / kanun
# zap - cut off, almost like hold strings and pluck at same time. dampened sound.
# marimba
# bug - interesting effect, hold over notes, lots of really sharp vibrato
# pluse - almost sounds like sine wave, close to a really loud and annoying clarinet.
# saw - saw wave (sounds almost like bad alto )
# snick - xylophones in back, bad drums in front
# twang - so out of tune it hurts
# karp - almost like a harp, plucked guitar
# arpy - buzzy and quickly diminishing string
# nylon - not terrible, but sounds synthetic. like a bad keyboard sound, with lots of buzz
# donk - if want to do with percussion like tabla, or really low flute
# swell - sort of like a brass section sounds like, really heavy on the brassy-ness
# razz - sounds a little like a woodwind section, if you could squint with your ears
# sitar - harshly plucked string, but not very much of the cool reverb of sitar
# jbass - almost like some low woodwinds (bass clarinet?, bari sax)
# sawbass - growly sounding bass, with too much exposure on amp, sometimes used in blues
# prophet - new agey
# pads - synth. piano sound
# ambi - organ
# space - high pitched orcarina like sound often used in space music, almost like whistle
# keys - piano
# sinepad - xylaphone like
