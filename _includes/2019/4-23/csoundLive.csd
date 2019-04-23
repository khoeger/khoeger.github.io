;; Select this code and press ctrl-e to evaluate
;; reset_clock()
set_tempo(100)
set_scale("maj")

;; callback instrument for csound-live-code
instr P1
  ;--- drums
  ; snare
  hexplay(	"1002",
      		"SD", p3,
      		in_scale(-1, 0),
      		fade_in(7, 128) * ampdbfs(-12))
  ; bass drum
  hexplay(	"1111",
      		"BD", p3,
      		in_scale(-1, 0),
      		fade_in(8, 128) * ampdbfs(-6))
  ; open high hat
  hexplay("1000",
      "0HH", p3,
      in_scale(-1, 0),
      fade_in(9, 128) * ampdbfs(-5))

    ;--- bass linked
    ; pickup note
  	hexplay("10000000",
      		"Sub5", p3,
      		in_scale(-1, 1.5),
      		fade_in(11, 128) * ampdbfs(-12))
    ; first note
	   hexplay("01000000",
      		"Sub5", p3,
      		in_scale(-1, 0),
      		fade_in(11, 128) * ampdbfs(-12))
    ; second note
    hexplay(	"00200000",
      		"Sub5", p3,
      		in_scale(-1, 1.5),
      		fade_in(11, 128) * ampdbfs(-12))
    ; third note
    hexplay(	"00020000",
      		"Sub5", p3,
      		in_scale(-1, 2),
      		fade_in(11, 128) * ampdbfs(-12))
    ; fourth note
	  hexplay("00001000",
      		"Sub5", p3,
      		in_scale(-1, 3.5),
      		fade_in(11, 128) * ampdbfs(-12))

endin
