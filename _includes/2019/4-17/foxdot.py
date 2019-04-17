Clock.bpm = 60
Scale.default.set("major")
# -- Pitches for each phrase
# 1
pphrase1 = P[0, 2, 3, 3.5, 4]
# 2
pphrase2 = P[7, 5.5, 5, 4,  5]
# 3
pphrase3 = P[7, 5.5, 7, 7, 7, 7, 8]
# Ending
pphrase4 = P[7, 5.5, 5, 4, 5, 0, 1, 1.5, 1, 0]

# -- Durations for each phrase
# 1
rphrase1 = P[1, 2/3, 1/3, 1/2, 3/2 ]
# 2
rphrase2 = P[1, 2/3, 1/3, 1/2, 3/2 + 1/3]
# 3
rphrase3 = P[1/3, 2/3, 3/2, 2/3, 1, 2/3, 3/2 + 2/3]
# Ending
rphrase4 = P[1, 2/3, 1/3, 2/3, 1/3, 2/3, 1/3, 1, 2/3, 1/3 + 2]

# -- Melody, plucked guitar
# By intervals, 0 is C, 2 is E, so on ..
s1 >> pluck(    # Pitches
                pphrase1  | pphrase2  | pphrase3  | pphrase4,
                # Durations
                dur = [rphrase1 | rphrase2 | rphrase3 | rphrase4],
                amp = 0.75, # Amplitude
                lpf = 700,  # low and high pass filters: cuts a frequency range
                hpf = 300   #     out for pluck to be heard & not compete
            )

db >> dbass(    # Pitches
                pphrase1  | pphrase2  | pphrase3  | pphrase4,
                # Durations
                dur = rphrase1 | rphrase2 | rphrase3 | rphrase4,
                amp = 0.75 , # Amplitude
                lpf= 300    #double bass is now alone in freq. range
              )

# no rests! not sure how to add them, so just extended notes too long.
s1.stop()

db.stop()
