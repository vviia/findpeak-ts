import numpy as np
ppg = np.array([100,
118,
141,
169,
200,
234,
268,
305,
342,
380,
417,
450,
483,
516,
545,
574,
600,
624,
646,
667,
686,
703,
717,
732,
742,
753,
762,
768,
775,
777,
781,
783,
781,
778,
776,
774,
768,
762,
755,
748,
740,
730,
721,
713,
701,
692,
681,
672,
661,
649,
640,
625,
615,
606,
595,
586,
578,
569,
560,
550,
540,
533,
526,
519,
511,
503,
495,
488,
480,
476,
466,
457,
448,
438,
431,
421,
413,
406,
397,
387,
380,
373,
365,
358,
349,
341,
333,
323,
316,
309,
299,
289,
283,
274,
265,
256,
249,
241,
231,
222,
215,
207,
198,
190,
182,
172,
162,
156,
147,
138,
131,
120,
109,
98,
91,
81,
73,
65,
57,
53,
45,
43,
40,
41,
42,
48,
64,
78,
99,
126,
158,
191,
226,
264,
304,
344,
383,
425,
464,
501,
536,
569,
601,
629,
656,
681,
703,
723,
738,
755,
769,
780,
786,
797,
802,
808,
813,
814,
816,
816,
816,
813,
808,
803,
800,
791,
783,
776,
766,
755,
743,
730,
719,
706,
693,
681,
670,
657,
646,
636,
625,
614,
603,
596,
584,
575,
566,
558,
549,
540,
532,
524,
512,
502,
493,
485,
474,
464,
458,
448,
438,
429,
421,
413,
403,
392,
385,
374,
365,
354,
347,
338,
327,
318,
311,
302,
292,
284,
277,
269,
262,
255,
249,
241,
235,
229,
221,
214,
205,
200,
191,
182,
174,
164,
152,
144,
137,
130,
123,
115,
111,
101,
95,
89,
83,
79,
78,
77,
80,
85,
95,
110,
129,
153,
179,
211,
247,
283,
321,
361,
400,
438,
476,
513,
546,
577,
607,
635,
660,
682,
703,
722,
737,
751,
761,
771,
779,
786,
795,
797,
800,
802,
804,
800,
799,
796,
794,
787,
780,
773,
766,
756,
745,
733,
720,
707,
697,
683,
670,
658,
646,
635,
624,
614,
602,
594,
582,
571,
563,
556,
546,
539,
531,
522,
511,
502,
495,
485,
477,
470,
460,
453,
443,
433,
425,
416,
408,
399,
391,
381,
372,
365,
354,
342,
330,
320,
310,
301,
290,
282,
271,
262,
254,
246,
238,
231,
225,
218,
210,
202,
195,
188,
181,
172,
166,
158,
150,
142,
137,
130,
122,
116,
109,
104,
97,
91,
86,
80,
75,
72,
67,
65,
64,
67,
70,
79,
92,
114,
140,
168,
202,
242,
280,
320,
362,
406,
444,
483,
525,
560,
594,
627,
656,
682,
704,
726,
747,
764,
781,
796,
808,
818,
825,
834,
841,
844,
847,
847,
848,
848,
841,
839,
833,
824,
815,
804,
794,
784,
771,
761,
747,
733,
720,
707,
692,
678,
665,
653,
636,
622,
612,
600,
587,
575,
564,
553,
541,
532,
524,
513,
504,
495,
489,
479,
471,
463,
454,
445,
437,
430,
421,
413,
403,
394,
382,
370,
361,
352,
341,
332,
324,
315,
306,
296,
288,
281,
272,
264,
256,
247,
238,
230,
223,
215,
203,
194,
186,
178,
168,
162,
155,
145,
137,
131,
123,
116,
108,
102,
95,
88,
81,
77,
71,
65,
57,
52,
48,
45,
46,
47,
51,
63,
78,
99,
124,
154,
191,
230,
270,
312,
355,
399,
441,
483,
522,
557,
592,
625,
658,
687,
711,
736,
758,
776,
794,
810,
823,
833,
842,
849,
855,
857,
861,
861,
857,
853,
848,
845,
837,
829,
821,
812,
801,
789,
778,
765,
753,
738,
729,
714,
700,
684,
673,
656,
641,
627,
616,
601,
589,
578,
565,
553,
541,
532,
521,
512,
502,
494,
484,
474,
465,
458,
448,
438,
427,
418,
407,
397,
388,
378,
369,
359,
351,
340,
332,
321,
311,
303,
293,
280,
273,
264,
253,
242,
233,
223,
212,
205,
197,
187,
177,
170,
163,
155,
146,
139,
131,
123,
114,
108,
101,
91,
86,
79,
71,
62,
58,
53,
47,
42,
41,
36,
32,
31,
33,
34,
38,
44,
59,
75,
98,
124,
158,
194,
232,
275,
320,
364,
409,
454,
497,
540,
578,
619,
653,
687,
715,
746,
770,
792,
813,
833,
848,
860,
869,
878,
883,
888,
892,
893,
893,
891,
890,
886,
880,
873,
865,
855,
844,
832,
821,
806,
793,
779,
765,
747,
731,
718,
703,
689,
675,
662,
649,
636,
623,
611,
599,
588,
577,
568,
557,
547,
538,
530,
515,
503,
494,
483,
473,
464,
453,
441,
432,
422,
411,
401,
391,
379,
368,
358,
346,
336,
326,
316,
302,
292,
281,
269,
258,
249,
238,
228,
217,
209,
198,
188,
177,
167,
158,
148,
140,
132,
121,
112,
103,
95,
87,
80,
74,
68,
61,
58,
54,
49,
46,
41,
39,
36,
34,
33,
35,
37,
41,
50,
61,
76,
99,
125,
158,
197,
235,
281,
325,
370,
415,
461,
504,
547,
587,
625,
659,
691,
720,
748,
769,
790,
808,
825,
841,
852,
862,
869,
875,
880,
883,
884,
883,
881,
879,
874,
866,
860,
851,
840,
824,
811,
798,
782,
768,
752,
735,
721,
705,
691,
677,
663,
650,
635,
623,
610,
600,
588,
576,
564,
551,
540,
529,
518,
509,
499,
490,
480,
473,
464,
454,
445,
435,
426,
416,
408,
399,
389,
378,
368,
356,
345,
334,
326,
315,
303,
292,
284,
273,
263,
253,
244,
232,
224,
216,
207,
198,
190,
181,
172,
161,
154,
147,
139,
132,
124,
116,
111,
104,
98,
94,
87,
84,
80,
76,
72,
68,
66,
65,
66,
68,
75,
87,
104,
125,
153,
186,
223,
262,
306,
349,
393,
441,
485,
526,
567,
606,
642,
675,
706,
734,
758,
781,
800,
820,
835,
848,
860,
871,
881,
886,
890,
893,
893,
894,
893,
890,
885,
879,
874,
862,
850,
839,
825,
811,
796,
783,
768,
753,
738,
724,
708,
694,
679,
666,
652,
639,
625,
612,
597,
582,
570,
561,
548,
536,
526,
516,
504,
493,
479,
469,
457,
444,
434,
422,
411,
400,
389,
377,
365,
352,
342,
330,
321,
309,
300,
287,
275,
267,
258,
247,
236,
227,
217,
206,
197,
188,
179,
171,
159,
151,
143,
134,
126,
119,
110,
104,
97,
93,
85,
80,
75,
69,
64,
60,
55,
51,
45,
41,
41,
38,
35,
36,
42,
50,
62,
82,
109,
137,
171,
212,
253,
296,
341,
387,
432,
477,
523,
564,
604,
635,
669,
703,
727,
753,
775,
797,
816,
832,
848,
858,
869,
877,
885,
891,
895,
896,
898,
897,
895,
889,
884,
877,
868,
860,
851,
840,
828,
814,
802,
787,
773,
760,
746,
732,
717,
704,
690,
676,
661,
649,
634,
623,
610,
598,
588,
576,
565,
555,
545,
534,
524,
516,
503,
491,
483,
472,
460,
449,
439,
423,
410,
398,
382,
372,
356,
345,
332,
318,
306,
295,
284,
272,
261,
252,
241,
230,
219,
209,
198,
185,
176,
167,
156,
147,
140,
132,
124,
116,
109,
102,
96,
89,
84,
78,
71,
66,
62,
57,
49,
44,
39,
35,
33,
32,
37,
40,
50,
66,
86,
108,
139,
171,
208,
248,
293,
335,
378,
423,
460,
502,
538,
574,
610,
644,
671,
700,
725,
746,
766,
784,
800,
815,
824,
833,
841,
846,
848,
852,
851,
849,
846,
843,
842,
833,
827,
822,
812,
803,
793,
781,
768,
755,
743,
730,
716,
702,
689,
675,
659,
644,
632,
619,
606,
595,
586,
577,
566,
556,
549,
538,
530,
521,
513,
503,
493,
485,
477,
468,
455,
446,
435,
424,
413,
405,
396,
385,
375,
368,
358,
348,
335,
326,
318,
308,
297,
289,
276,
264,
253,
243,
232,
221,
213,
204,
194,
185,
176,
169,
159,
152,
147,
138,
128,
122,
116,
107,
102,
94,
85,
78,
68,
63,
59,
53,
50,
47,
45,
47,
52,
61,
74,
91,
114,
143,
178,
215,
254,
297,
334,
377,
419,
460,
499,
539,
578,
610,
642,
671,
698,
723,
743,
763,
782,
795,
808,
821,
829,
834,
839,
843,
846,
846,
844,
844,
842,
837,
831,
827,
819,
812,
800,
790,
780,
765,
755,
742,
725,
710,
697,
682,
670,
655,
644,
629,
618,
605,
593,
582,
571,
560,
550,
542,
531,
522,
514,
503,
492,
481,
470,
461,
451,
443,
434,
425,
414,
407,
397,
388,
379,
370,
362,
354,
345,
336,
328,
312,
302,
294,
281,
273,
264,
254,
244,
238,
229,
220,
212,
203,
196,
187,
179,
171,
167,
156,
149,
140,
130,
120,
113,
106,
95,
89,
83,
76,
68,
61,
57,
55,
52,
52,
56,
65,
77,
97,
120,
149,
177,
212,
250,
290,
329,
372,
413,
452,
494,
529,
567,
597,
628,
656,
682,
703,
724,
741,
759,
770,
782,
791,
800,
805,
809,
813,
816,
816,
816,
816,
813,
807,
802,
796,
789,
777,
768,
759,
747,
732,
721,
707,
694,
680,
668,
655,
643,
631,
620,
609,
599,
589,
579,
571,
562,
555,
546,
539,
527,
521,
512,
504,
495,
488,
478,
471,
462,
454,
446,
436,
429,
419,
411,
399,
391,
384,
372,
363,
350,
339,
331,
319,
312,
302,
294,
285,
277,
266,
261,
252,
245,
236,
229,
221,
213,
204,
195,
187,
178,
170,
161,
154,
146,
137,
129,
123,
114,
108,
100,
97,
92,
91,
92,
98,
108,
122,
143,
166,
192,
222,
258,
296,
332,
370,
410,
447,
485,
518,
554,
584,
612,
642,
664,
689,
708,
727,
742,
756,
764,
777,
784,
791,
796,
801,
801,
802,
801,
801,
796,
794,
788,
784,
776,
767,
762,
751,
740,
726,
716,
704,
692,
680,
669,
655,
644,
635,
623,
612,
603,
594,
585,
576,
569,
560,
552,
544,
536,
528,
519,
510,
500,
493,
484,
478,
468,
461,
451,
442,
435,
426,
418,
410,
400,
390,
382,
372,
361,
353,
341,
333,
325,
317,
308,
299,
294,
285,
278,
272,
265,
256,
247,
242,
237,
227,
220,
215,
207,
197,
189,
183,
175,
167,
161,
154,
145,
138,
132,
124,
120,
113,
112,
111,
111,
116,
126,
141,
160,
183,
209,
238,
271,
304,
341,
374,
410,
445,
478,
510,
539,
570,
595,
621,
643,
663,
684,
699,
715,
728,
738,
747,
756,
763,
766,
772,
777,
777,
778,
778,
776,
775,
771,
766,
762,
755,
747,
740,
734,
718,
706,
695,
683,
672,
661,
648,
637,
626,
616,
605,
596,
585,
575,
566,
558,
551,
544,
536,
529,
520,
513,
505,
498,
488,
483,
475,
467,
458,
451,
441,
434,
425,
416,
409,
398,
391,
382,
372,
361,
352,
344,
333,
326,
318,
310,
303,
295,
287,
280,
274,
265,
261,
255,
247,
240,
235,
229,
220,
214,
207,
201,
195,
189,
182,
176,
168,
162,
157,
148,
143,
136,
129,
123,
119,
117,
117,
120,
128,
140,
156,
177,
201,
227,
258,
289,
323,
356,
387,
421,
454,
483,
511,
539,
565,
588,
608,
632,
647,
663,
678,
690,
704,
713,
723,
732,
738,
743,
748,
751,
753,
755,
754,
755,
750,
747,
743,
739,
728,
717,
713,
703,
694,
685,
673,
664,
654,
642,
634,
624,
613,
603,
594,
584,
575,
565,
559,
548,
538,
529,
523,
513,
505,
498,
489,
482,
474,
468,
460,
451,
444,
438,
429,
422,
415,
411,
401,
389,
381,
371,
359,
351,
344,
335,
327,
321,
313,
304,
295,
285,
281,
269,
261,
254,
248,
239,
230,
222,
213,
204,
196,
190,
183,
177,
169,
162,
156,
150,
143,
140,
131,
123,
117,
112,
106,
98,
94,
86,
82,
78,
81,
85,
93,
107,
125,
144,
169,
199,
230,
264,
299,
334,
369,
404,
437,
470,
499,
525,
552,
577,
602,
623,
640,
660,
676,
689,
703,
712,
722,
730,
738,
745,
745,
748,
752,
752,
751,
745,
745,
738,
734,
728,
725,
716,
708,
701,
694,
685,
673,
665,
657,
645,
635,
627,
617,
608,
596,
586,
575,
567,
557,
550,
541,
532,
525,
518,
509,
501,
493,
487,
481,
472,
465,
456,
448,
438,
430,
421,
411,
401,
394,
383,
376,
367,
360,
351,
343,
336,
330,
322,
314,
307,
299,
292,
283,
277,
269,
259,
253,
244,
235,
228,
221,
216,
207,
200,
195,
189,
181,
173,
170,
161,
156,
149,
141,
133,
125,
115,
110,
101,
93,
87,
82,
78,
76,
77,
82,
88,
102,
121,
143,
169,
199,
231,
267,
303,
339,
378,
413,
446,
480,
514,
544,
571,
600,
625,
648,
669,
689,
705,
721,
734,
748,
756,
765,
772,
779,
781,
782,
781,
784,
781,
778,
776,
771,
766,
758,
751,
745,
735,
724,
714,
702,
692,
679,
666,
654,
639,
627,
614,
601,
590,
578,
570,
558,
549,
542,
533,
523,
516,
510,
502,
494,
488,
482,
474,
466,
461,
449,
441,
433,
426,
421,
412,
404,
398,
393,
386,
379,
373,
366,
360,
352,
347,
339,
333,
326,
318,
310,
303,
297,
288,
282,
274,
270,
262,
254,
248,
242,
235,
227,
219,
213,
205,
199,
189,
181,
171,
160,
152,
142,
135,
127,
121,
116,
114,
112,
114,
118,
129,
143,
161,
185,
212,
242,
276,
311,
345,
381,
417,
452,
486,
521,
552,
581,
609,
636,
659,
681,
702,
718,
734,
747,
760,
772,
779,
785,
790,
793,
794,
794,
794,
794,
791,
786,
782,
775,
769,
760,
751,
742,
731,
721,
710,
697,
685,
673,
663,
646,
632,
622,
612,
599,
587,
580,
569,
559,
553,
545,
536,
528,
521,
514,
505,
496,
490,
482,
472,
462,
454,
445,
437,
427,
421,
413,
408,
399,
392,
383,
375,
368,
360,
352,
344,
336,
331,
321,
313,
303,
296,
284,
277,
269,
263,
253,
246,
240,
231,
226,
217,
211,
203,
196,
190,
182,
174,
168,
160,
151,
142,
136,
126,
120,
112,
103,
100,
93,
88,
84,
84,
86,
92,
103,
118,
136,
162,
192,
223,
259,
295,
334,
372,
412,
448,
486,
520,
554,
587,
618,
646,
672,
695,
716,
735,
753,
767,
780,
793,
797,
805,
809,
813,
815,
817,
818,
816,
814,
814,
808,
802,
796,
789,
780,
771,
761,
750,
740,
729,
713,
700,
686,
674,
663,
650,
638,
627,
618,
605,
594,
585,
575,
565,
555,
548,
538,
529,
521,
512,
500,
491,
482,
473,
464,
456,
449,
439,
431,
421,
413,
404,
394,
385,
377,
369,
359,
349,
341,
332,
322,
311,
303,
293,
284,
276,
267,
260,
250,
242,
237,
228,
220,
213,
206,
199,
188,
182,
173,
165,
155,
148,
137,
129,
120,
114,
106,
99,
94,
88,
81,
75,
70,
65,
58,
56,
54,
55,
59,
66,
78,
94,
115,
142,
176,
212,
250,
289,
331,
371,
411,
452,
490,
527,
562,
595,
626,
654,
679,
705,
722,
740,
757,
772,
784,
796,
804,
814,
820,
824,
827,
829,
830,
829,
829,
824,
821,
814,
810,
801,
791,
780,
771,
759,
747,
735,
723,
712,
701,
689,
677,
664,
654,
644,
631,
621,
610,
602,
592,
582,
571,
563,
552,
541,
533,
526,
517,
508,
500,
493,
483,
474,
466,
458,
448,
436,
429,
421,
411,
402,
390,
380,
371,
360,
352,
342,
333,
325,
316,
307,
297,
289,
280,
271,
263,
256,
247,
238,
229,
222,
210,
202,
194,
186,
177,
169,
160,
154,
146,
137,
130,
120,
114,
106,
100,
92,
86,
77,
72,
62,
58,
55,
52,
53,
56,
66,
80,
99,
121,
152,
185,
220,
259,
299,
340,
381,
423,
463,
499,
533,
568,
598,
630,
656,
682,
705,
726,
745,
763,
778,
790,
802,
811,
819,
823,
828,
832,
834,
832,
832,
827,
821,
817,
811,
806,
794,
785,
776,
765,
754,
742,
732,
718,
705,
691,
679,
664,
651,
638,
626,
610,
596,
584,
572,
560,
550,
541,
530,
520,
510,
502,
493,
484,
473,
468,
457,
448,
438,
431,
421,
408,
397,
388,
376,
364,
354,
343,
332,
321,
311,
300,
290,
281,
273,
262,
254,
241,
235,
225,
216,
206,
197,
187,
178,
172,
165,
157,
152,
146,
137,
131,
124,
118,
111,
104,
98,
91,
86,
79,
75,
68,
60,
53,
48,
44,
41,
36,
33,
33,
33,
36,
45,
59,
77,
99,
128,
161,
196,
236,
277,
319,
361,
405,
445,
486,
528,
564,
600,
633,
662,
691,
717,
740,
761,
782,
797,
811,
822,
837,
840,
845,
852,
853,
854,
854,
852,
851,
848,
842,
836,
828,
817,
809,
798,
788,
775,
761,
749,
732,
716,
703,
689,
675,
661,
650,
638,
625,
614,
602,
591,
580,
568,
560,
550,
539,
532,
525,
513,
500,
491,
483,
473,
463,
456,
447,
437,
428,
420,
409,
401,
392,
384,
373,
363,
353,
345,
335,
325,
314,
302,
294,
282,
273,
263,
254,
246,
237,
229,
221,
213,
206,
197,
190,
183,
177,
170,
164,
156,
148,
139,
130,
122,
116,
107,
100,
95,
90,
83,
78,
74,
72,
70,
72,
78,
85,
98,
117,
142,
169,
200,
236,
274,
315,
356,
401,
441,
483,
522,
562,
596,
630,
663,
692,
719,
743,
766,
785,
802,
816,
825,
835,
842,
848,
854,
856,
858,
857,
857,
854,
848,
843,
837,
827,
817,
807,
796,
783,
769,
754,
739,
724,
711,
695,
681,
665,
654,
640,
628,
615,
604,
594,
583,
571,
564,
554,
544,
534,
525,
516,
507,
495,
487,
477,
467,
458,
449,
438,
428,
418,
408,
398,
387,
377,
368,
356,
347,
336,
326,
315,
300,
290,
280,
270,
258,
249,
239,
229,
220,
212,
202,
195,
186,
179,
169,
163,
156,
150,
141,
129,
125,
117,
109,
102,
96,
90,
85,
80,
75,
70,
65,
62,
59,
54,
51,
49,
49,
49,
50,
58,
67,
79,
98,
126,
157,
191,
232,
276,
321,
366,
411,
457,
500,
544,
585,
625,
658,
691,
723,
751,
776,
796,
820,
837,
852,
865,
879,
887,
894,
900,
904,
904,
908,
904,
903,
896,
892,
884,
877,
866,
852,
840,
826,
813,
800,
787,
772,
757,
744,
730,
716,
703,
690,
677,
662,
650,
638,
628,
617,
601,
591,
580,
568,
558,
548,
537,
525,
515,
506,
494,
481,
470,
461,
448,
436,
427,
415,
402,
390,
377,
364,
352,
340,
329,
315,
305,
293,
282,
271,
262,
251,
240,
229,
220,
211,
202,
192,
181,
172,
163,
153,
144,
136,
129,
120,
112,
108,
98,
93,
88,
81,
76,
72,
68,
60,
55,
50,
46,
40,
33,
27,
27,
24,
22,
23,
29,
36,
50,
67,
93,
120,
154,
194,
235,
278,
322,
369,
415,
457,
500,
543,
581,
619,
652,
685,
716,
743,
768,
791,
812,
830,
845,
860,
868,
879,
887,
893,
896,
901,
897,
898,
894,
891,
887,
883,
876,
868,
861,
851,
840,
828,
817,
804,
791,
779,
767,
752,
737,
722,
706,
691,
679,
665,
653,
640,
627,
616,
605,
594,
584,
575,
564,
553,
543,
536,
524,
514,
500,
487,
477,
465,
453,
444,
432,
421,
410,
397,
385,
377,
366,
355,
345,
333,
323,
312,
303,
290,
282,
267,
256,
247,
238,
226,
216,
207,
198,
189,
180,
171,
163,
154,
146,
139,
130,
122,
113,
105,
97,
87,
79,
75,
67,
61,
58,
50,
45,
39,
35,
34,
29,
32,
32,
34,
41,
55,
73,
93,
121,
155,
191,
229,
273,
317,
361,
406,
452,
497,
537,
576,
615,
650,
681,
711,
738,
764,
786,
804,
821,
832,
843,
854,
862,
868,
873,
876,
880,
879,
878,
879,
874,
868,
860,
855,
847,
835,
827,
815,
799,
785,
771,
758,
743,
730,
716,
703,
688,
674,
662,
648,
637,
625,
611,
601,
588,
576,
565,
552,
539,
530,
521,
508,
496,
487,
478,
464,
454,
444,
434,
424,
413,
405,
393,
382,
371,
362,
352,
339,
327,
319,
307,
297,
287,
279,
267,
257,
248,
238,
229,
218,
212,
202,
193,
183,
176,
167,
159,
148,
140,
130,
120,
111,
105,
94,
87,
80,
72,
64,
58,
53,
49,
42,
37,
36,
30,
26,
22,
23,
22,
26,
35,
50,
67,
92,
121,
156,
193,
235,
279,
323,
369,
416,
459,
503,
541,
579,
614,
647,
677,
707,
732,
754,
776,
796,
813,
826,
838,
850,
857,
862,
868,
873,
873,
874,
873,
867,
859,
853,
846,
838,
826,
816,
805,
793,
778,
765,
753,
738,
725,
709,
696,
682,
670,
656,
644,
628,
616,
603,
591,
581,
572,
561,
552,
541,
531,
525,
516,
507,
498,
492,
483,
474,
463,
453,
445,
433,
423,
413,
401,
390,
380,
371,
358,
347,
338,
326,
315,
304,
294,
284,
272,
262,
252,
242,
233,
219,
209,
200,
189,
183,
174,
166,
155,
149,
139,
132,
123,
116,
107,
100,
94,
88,
80,
73,
68,
61,
55,
49,
48,
46,
44,
46,
55,
66,
82,
103,
132,
163,
197,
237,
282,
322,
367,
408,
453,
492,
531,
568,
603,
635,
666,
693,
722,
743,
765,
784,
799,
814,
824,
836,
842,
848,
852,
854,
855,
850,
847,
843,
835,
829,
821,
809,
799,
787,
776,
762,
747,
733,
721,
708,
693,
678,
666,
652,
640,
627,
613,
600,
590,
580,
569,
559,
549,
544,
535,
524,
517,
506,
498,
489,
479,
472,
461,
450,
441,
432,
420,
409,
399,
389,
379,
371,
362,
353,
344,
334,
325,
317,
307,
296,
288,
279,
269,
261,
252,
242,
228,
221,
213,
202,
193,
185,
177,
169,
161,
155,
149,
141,
132,
125,
119,
113,
106,
100,
93,
85,
78,
69,
63,
59,
54,
53,
52,
52,
60,
72,
88,
108,
136,
165,
203,
242,
287,
328,
371,
417,
461,
499,
540,
578,
616,
650,
682,
711,
737,
763,
783,
802,
820,
834,
848,
859,
868,
876,
882,
885,
887,
886,
884,
881,
879,
872,
866,
859,
850,
838,
829,
817,
804,
792,
780,
765,
753,
739,
727,
714,
699,
684,
672,
658,
644,
634,
621,
609,
597,
587,
576,
568,
556,
547,
536,
528,
519,
509,
499,
488,
478,
466,
454,
444,
432,
420,
408,
397,
389,
378,
369,
357,
349,
338,
327,
318,
309,
299,
288,
276,
265,
256,
246,
237,
229,
220,
213,
205,
196,
187,
179,
171,
164,
154,
148,
141,
133,
125,
119,
110,
103,
96,
91,
86,
80,
75,
70,
65,
64,
62,
65,
68,
76,
90,
108,
133,
159,
195,
229,
264,
303,
347,
387,
429,
469,
509,
549,
585,
620,
653,
683,
711,
738,
762,
781,
800,
817,
832,
844,
850,
860,
864,
869,
872,
875,
875,
874,
872,
871,
864,
857,
850,
842,
832,
819,
809,
797,
784,
772,
754,
740,
726,
712,
701,
686,
673,
662,
651,
639,
628,
617,
608,
597,
586,
578,
569,
557,
547,
534,
523,
512,
500,
491,
481,
469,
458,
446,
436,
426,
415,
405,
392,
383,
375,
364,
353,
345,
333,
322,
311,
300,
292,
282,
272,
263,
256,
247,
238,
231,
225,
215,
207,
200,
191,
184,
175,
169,
160,
153,
144,
135,
127,
119,
111,
107,
99,
91,
85,
78,
71,
63,
59,
54,
46,
45,
44,
47,
52,
61,
77,
96,
125,
153,
187,
223,
259,
299,
341,
380,
419,
456,
493,
528,
561,
591,
619,
644,
667,
685,
704,
722,
736,
750,
761,
770,
779,
786,
790,
793,
796,
800,
797,
796,
793,
791,
786,
777,
771,
763,
750,
739,
729,
716,
703,
690,
679,
664,
652,
640,
629,
616,
604,
594,
584,
571,
562,
552,
542,
532,
520,
511,
502,
491,
483,
476,
464,
455,
447,
438,
429,
421,
414,
404,
397,
389,
381,
371,
363,
354,
346,
335,
328,
319,
311,
302,
293,
286,
280,
271,
261,
257,
247,
238,
230,
224,
217,
208,
201,
191,
181,
173,
164,
156,
148,
141,
133,
129,
120,
110,
104,
98,
91,
83,
79,
73,
65,
60,
60,
56,
49,
53,
60,
69,
85,
103,
128,
160,
191,
229,
267,
307,
344,
386,
424,
462,
498,
534,
564,
596,
620,
648,
671,
689,
712,
729,
744,
757,
771,
783,
791,
797,
806,
808,
811,
813,
813,
810,
808,
805,
797,
789,
779,
773,
763,
752,
739,
728,
717,
703,
690,
680,
666,
653,
641,
631,
618,
606,
595,
585,
573,
562,
551,
545,
533,
525,
518,
510,
501,
493,
485,
477,
467,
460,
452,
444,
434,
427,
420,
410,
397,
388,
380,
368,
359,
349,
341,
331,
322,
316,
308,
299,
290,
282,
275,
265,
259,
251,
244,
236,
227,
220,
213,
204,
198,
190,
185,
178,
172,
166,
160,
154,
148,
140,
134,
129,
123,
116,
111,
108,
106,
101,
102,
108,
120,
136,
157,
185,
214,
247,
284,
323,
361,
401,
439,
478,
515,
551,
584,
616,
643,
667,
692,
714,
734,
750,
766,
781,
789,
800,
809,
816,
819,
821,
824,
824,
823,
821,
819,
813,
809,
798,
789,
780,
768,
757,
746,
734,
721,
712,
697,
685,
672,
661,
649,
635,
626,
616,
604,
595,
583,
575,
563,
554,
546,
538,
530,
521,
515,
506,
498,
490,
482,
473,
464,
456,
447,
437,
427,
419,
408,
396,
385,
376,
366,
357,
346,
338,
327,
318,
308,
300,
289,
280,
272,
263,
255,
245,
237,
226,
217,
209,
201,
193,
183,
177,
170,
161,
151,
143,
137,
126,
119,
111,
101,
93,
86,
78,
72,
66,
58,
54,
54,
57,
65,
80,
98,
121,
151,
186,
220,
257,
299,
341,
380,
422,
461,
501,
534,
568,
596,
626,
651,
677,
700,
721,
736,
752,
770,
782,
792,
801,
808,
814,
817,
821,
820,
821,
819,
818,
809,
801,
793,
784,
774,
762,
751,
741,
728,
717,
704,
694,
681,
670,
660,
648,
636,
626,
616,
605,
594,
586,
575,
566,
558,
549,
542,
533,
526,
517,
510,
500,
492,
485,
477,
469,
459,
450,
440,
428,
418,
409,
398,
390,
379,
372,
361,
352,
343,
334,
324,
315,
306,
296,
286,
276,
268,
258,
249,
236,
230,
222,
213,
205,
198,
190,
181,
174,
169,
160,
153,
146,
140,
131,
124,
117,
110,
103,
93,
87,
81,
75,
73,
74,
78,
85,
98,
118,
140,
169,
202,
237,
272,
309,
347,
386,
423,
460,
497,
528,
560,
589,
618,
645,
669,
693,
716,
732,
749,
764,
777,
789,
797,
807,
812,
817,
820,
823,
821,
820,
815,
814,
809,
803,
795,
788,
778,
768,
758,
748,
737,
725,
713,
704,
689,
677,
667,
655,
641,
627,
618,
605,
594,
583,
574,
563,
553,
545,
536,
525,
515,
508,
497,
488,
480,
469,
460,
451,
441,
429,
417,
407,
397,
388,
378,
369,
359,
350,
338,
329,
320,
310,
300,
289,
281,
271,
262,
252,
244,
232,
221,
213,
206,
197,
189,
181,
172,
165,
158,
150,
144,
137,
128,
121,
111,
104,
94,
87,
81,
72,
65,
60,
53,
49,
50,
51,
57,
68,
83,
104,
130,
160,
192,
229,
267,
305,
347,
386,
421,
458,
495,
527,
559,
590,
618,
643,
666,
690,
708,
727,
740,
755,
767,
777,
784,
792,
797,
800,
800,
800,
797,
795,
792,
789,
782,
775,
769,
760,
750,
741,
730,
718,
706,
694,
682,
669,
656,
642,
630,
614,
602,
591,
578,
569,
558,
546,
538,
530,
520,
512,
503,
495,
485,
480,
470,
461,
452,
442,
432,
423,
413,
406,
396,
386,
377,
369,
358,
351,
341,
333,
322,
313,
305,
297,
288,
277,
271,
257,
250,
240,
231,
222,
214,
207,
199,
189,
181,
173,
166,
159,
149,
143,
133,
125,
116,
108,
99,
89,
80,
71,
65,
58,
52,
48,
46,
47,
51,
61,
74,
94,
120,
147,
179,
215,
254,
292,
331,
369,
409,
446,
482,
518,
552,
581,
611,
640,
662,
684,
703,
723,
737,
751,
761,
773,
780,
786,
792,
790,
792,
791,
788,
788,
784,
780,
776,
768,
759,
752,
742,
731,
721,
709,
697,
685,
673,
661,
648,
633,
621,
610,
599,
587,
577,
568,
557,
549,
540,
535,
525,
518,
510,
503,
494,
487,
479,
473,
461,
453,
442,
436,
427,
417,
410,
402,
393,
383,
375,
367,
357,
348,
341,
332,
322,
314,
305,
295,
285,
277,
269,
260,
250,
242,
234,
226,
217,
211,
202,
195,
186,
177,
170,
162,
155,
148,
140,
129,
119,
113,
105,
97,
95,
92,
91,
93,
104,
114,
132,
155,
184,
214,
249,
286,
325,
364,
403,
441,
477,
512,
547,
579,
610,
637,
664,
690,
710,
729,
745,
763,
777,
788,
797,
806,
811,
817,
820,
823,
818,
816,
812,
809,
802,
795,
788,
779,
769,
761,
750,
737,
725,
713,
703,
687,
675,
662,
652,
639,
625,
613,
602,
590,
579,
571,
561,
552,
544,
536,
527,
520,
511,
503,
496,
489,
480,
472,
461,
452,
440,
431,
421,
412,
400,
391,
381,
371,
363,
353,
344,
335,
327,
315,
306,
298,
289,
280,
270,
260,
251,
240,
230,
222,
212,
205,
196,
188,
180,
172,
164,
158,
149,
142,
135,
127,
120,
111,
105,
97,
87,
80,
74,
70,
68,
66,
73,
82,
97,
116,
140,
170,
201,
239,
279,
317,
357,
397,
437,
471,
506,
540,
573,
604,
631,
658,
682,
703,
722,
741,
756,
769,
783,
793,
802,
808,
814,
818,
816,
818,
818,
816,
812,
807,
803,
796,
789,
781,
774,
762,
752,
740,
730,
716,
705,
693,
682,
664,
654,
641,
629,
618,
606,
597,
587,
577,
566,
558,
549,
540,
532,
524,
517,
506,
499,
489,
479,
467,
457,
448,
437,
429,
420,
409,
399,
388,
380,
370,
362,
353,
343,
334,
325,
317,
307,
297,
290,
278,
269,
259,
251,
242,
235,
227,
217,
211,
203,
194,
189,
182,
174,
167,
159,
152,
145,
134,
128,
121,
111,
102,
96,
88,
83,
80,
80,
82,
88,
99,
116,
136,
162,
192,
225,
259,
296,
335,
373,
409,
444,
479,
513,
545,
576,
607,
631,
656,
678,
700,
716,
731,
748,
760,
770,
778,
789,
797,
800,
803,
804,
805,
802,
800,
798,
792,
789,
781,
775,
765,
758,
747,
737,
726,
715,
705,
692,
680,
668,
657,
641,
629,
616,
608,
595,
584,
575,
566,
556,
546,
541,
530,
520,
510,
501,
491,
482,
471,
465,
453,
442,
430,
425,
413,
403,
392,
385,
372,
362,
352,
344,
334,
323,
314,
304,
294,
285,
277,
269,
260,
248,
241,
230,
219,
210,
202,
193,
183,
174,
168,
158,
151,
145,
138,
131,
122,
117,
110,
103,
96,
90,
80,
73,
67,
64,
59,
59,
62,
66,
78,
91,
112,
137,
164,
198,
233,
268,
306,
345,
383,
417,
451,
485,
520,
548,
579,
604,
628,
650,
672,
691,
708,
722,
734,
746,
757,
763,
769,
776,
779,
778,
780,
782,
778,
773,
770,
767,
761,
754,
746,
736,
728,
715,
705,
692,
679,
668,
656,
642,
632,
621,
607,
595,
583,
574,
564,
556,
545,
537,
529,
520,
511,
505,
497,
487,
481,
476,
465,
459,
451,
445,
431,
425,
416,
407,
398,
390,
383,
375,
366,
359,
352,
344,
336,
326,
320,
312,
306,
297,
290,
280,
268,
261,
255,
245,
238,
231,
223,
216,
208,
202,
196,
187,
180,
174,
165,
159,
153,
145,
136,
128,
117,
114,
105,
101,
101,
102,
108,
119,
136,
155,
179,
208,
240,
271,
307,
342,
376,
412,
445,
477,
509,
533,
559,
586,
610,
629,
648,
667,
681,
694,
705,
718,
727,
734,
740,
744,
748,
750,
753,
753,
748,
744,
740,
733,
728,
721,
713,
705,
695,
686,
679,
664,
656,
645,
636,
624,
614,
604,
596,
586,
572,
562,
555,
546,
538,
532,
523,
517,
512,
506,
499,
492,
486,
480,
472,
466,
460,
455,
446,
439,
432,
423,
415,
408,
400,
393,
386,
377,
372,
366,
360,
353,
346,
339,
331,
327,
321,
314,
308,
302,
298,
288,
280,
274,
269,
263,
256,
250,
243,
237,
231,
226,
219,
212,
206,
201,
193,
187,
183,
177,
175,
173,
176,
182,
192,
206,
227,
249,
274,
303,
334,
365,
396,
428,
460,
489,
517,
545,
570,
594,
614,
637,
651,
668,
681,
695,
706,
715,
725,
731,
738,
744,
748,
750,
755,
754,
754,
752,
749,
745,
742,
731,
724,
716,
708,
698,
689,
678,
669,
658,
648,
638,
628,
616,
606,
596,
587,
576,
568,
559,
548,
538,
530,
523,
516,
510,
502,
496,
489,
484,
478,
473,
464,
459,
453,
446,
439,
432,
426,
416,
409,
398,
394,
384,
376,
370,
364,
355,
348,
340,
335,
328,
321,
314,
307,
301,
294,
289,
283,
274,
267,
260,
251,
243,
239,
232,
226,
219,
215,
207,
200,
194,
187,
180,
173,
166,
159,
151,
146,
141,
135,
134,
135,
140,
151,
165,
184,
207,
231,
261,
290,
321,
353,
383,
414,
446,
475,
503,
528,
555,
576,
593,
613,
630,
646,
660,
675,
687,
696,
705,
711,
719,
723,
727,
730,
732,
733,
733,
733,
730,
725,
722,
717,
708,
700,
694,
687,
678,
668,
658,
648,
638,
629,
620,
609,
600,
589,
581,
571,
563,
554,
544,
534,
526,
519,
511,
502,
494,
488,
479,
472,
466,
459,
452,
443,
436,
432,
423,
415,
407,
401,
393,
382,
375,
367,
357,
350,
343,
337,
329,
321,
313,
307,
296,
290,
282,
273,
265,
259,
254,
244,
235,
227,
222,
212,
204,
198,
191,
184,
176,
172,
166,
161,
154,
150,
141,
136,
132,
125,
119,
117,
113,
115,
117,
126,
139,
155,
175,
201,
228,
259,
289,
321,
355,
387,
417,
449,
481,
508,
534,
558,
580,
598,
618,
637,
650,
664,
676,
689,
698,
706,
714,
722,
725,
729,
731,
734,
733,
732,
732,
731,
726,
721,
717,
710,
703,
697,
689,
679,
672,
663,
656,
646,
637,
629,
621,
612,
604,
595,
586,
577,
567,
558,
551,
543,
535,
530,
523,
516,
508,
502,
495,
488,
482,
475,
468,
461,
454,
450,
441,
432,
425,
415,
407,
400,
392,
385,
377,
368,
361,
353,
345,
338,
333,
323,
313,
305,
300,
291,
282,
276,
265,
258,
251,
243,
239,
230,
224,
220,
211,
205,
198,
194,
186,
179,
172,
167,
159,
151,
146,
139,
133,
125,
120,
115,
115,
118,
128,
138,
155,
177,
203,
230,
262,
297,
330,
363,
401,
433,
467,
500,
526,
554,
580,
603,
626,
647,
664,
682,
696,
709,
721,
731,
740,
747,
752,
756,
760,
762,
764,
762,
762,
757,
752,
750,
743,
737,
730,
721,
715,
704,
693,
685,
675,
664,
652,
641,
633,
621,
611,
601,
589,
576,
566,
558,
548,
540,
531,
524,
515,
509,
501,
493,
485,
479,
470,
463,
455,
448,
441,
433,
425,
416,
406,
398,
387,
379,
371,
362,
353,
344,
339,
327,
319,
311,
303,
292,
282,
276,
268,
259,
250,
239,
229,
220,
212,
205,
196,
188,
181,
174,
166,
158,
151,
146,
138,
129,
124,
117,
109,
100,
92,
84,
79,
76,
74,
74,
79,
88,
102,
118,
139,
166,
198,
230,
264,
302,
338,
375,
410,
447,
478,
509,
537,
567,
592,
615,
637,
660,
676,
692,
707,
720,
731,
738,
747,
753,
757,
761,
764,
764,
761,
760,
755,
749,
744,
738,
730,
723,
712,
700,
692,
681,
669,
656,
645,
633,
620,
610,
600,
587,
576,
564,
554,
544,
537,
528,
517,
510,
503,
496,
489,
480,
473,
467,
456,
447,
440,
431,
423,
414,
406,
394,
387,
377,
368,
360,
349,
341,
333,
323,
317,
309,
298,
289,
282,
272,
265,
257,
247,
240,
229,
219,
213,
207,
199,
194,
188,
181,
175,
169,
166,
160,
155,
150,
144,
138,
133,
127,
125,
116,
110,
103,
99,
96,
94,
96,
103,
110,
125,
146,
170,
199,
232,
270,
307,
347,
387,
431,
469,
509,
543,
579,
610,
641,
670,
699,
721,
742,
764,
782,
796,
810,
824,
832,
842,
849,
857,
861,
863,
864,
863,
860,
858,
853,
848,
838,
832,
824,
813,
802,
789,
776,
762,
749,
734,
722,
708,
695,
681,
667,
650,
639,
628,
616,
604,
595,
585,
576,
566,
557,
550,
542,
532,
524,
516,
506,
496,
489,
481,
471,
459,
448,
439,
426,
416,
408,
400,
386,
377,
370,
358,
349,
338,
329,
321,
313,
304,
296,
285,
278,
267,
257,
247,
236,
228,
219,
209,
201,
194,
185,
177,
166,
159,
151,
145,
138,
134,
125,
119,
113,
107,
97,
91,
88,
83,
78,
77,
80,
86,
96,
110,
133,
158,
187,
219,
257,
293,
333,
373,
414,
453,
487,
522,
555,
586,
616,
644,
669,
692,
713,
732,
751,
766,
779,
792,
800,
809,
816,
821,
824,
825,
826,
825,
822,
818,
814,
808,
801,
794,
788,
775,
765,
753,
743,
731,
718,
706,
694,
680,
666,
655,
640,
628,
616,
605,
595,
584,
574,
566,
556,
548,
539,
532,
522,
514,
506,
498,
488,
479,
470,
459,
449,
439,
432,
420,
411,
402,
395,
384,
375,
365,
357,
348,
337,
329,
320,
312,
302,
293,
284,
272,
259,
249,
239,
227,
217,
210,
199,
190,
181,
175,
165,
158,
148,
141,
133,
126,
119,
112,
104,
94,
85,
79,
73,
63,
57,
53,
47,
43,
42,
38,
39,
44,
54,
67,
87,
112,
141,
174,
211,
246,
287,
326,
368,
410,
449,
489,
522,
560,
590,
620,
645,
671,
694,
714,
733,
749,
765,
778,
790,
801,
804,
812,
818,
820,
823,
823,
824,
823,
820,
818,
814,
806,
800,
792,
783,
774,
762,
752,
740,
728,
711,
698,
685,
672,
658,
646,
633,
622,
609,
598,
587,
577,
567,
558,
547,
538,
528,
520,
510,
501,
493,
480,
468,
458,
449,
438,
427,
418,
407,
397,
387,
375,
367,
356,
346,
337,
326,
315,
305,
295,
283,
272,
258,
249,
237,
227,
216,
207,
198,
187,
178,
168,
158,
150,
141,
133,
124,
115,
106,
98,
90,
79,
71,
64,
56,
50,
44,
35,
30,
25,
22,
18,
16,
17,
20,
25,
37,
52,
75,
102,
130,
166,
205,
247,
290,
336,
382,
425,
468,
511,
550,
588,
626,
657,
688,
714,
741,
762,
782,
799,
814,
826,
836,
844,
852,
857,
861,
864,
865,
864,
860,
858,
853,
845,
837,
828,
819,
805,
793,
776,
759,
743,
727,
714,
699,
684,
669,
654,
639,
622,
611,
598,
586,
573,
563,
554,
543,
533,
526,
513,
502,
491,
483,
475,
466,
457,
450,
441,
432,
423,
415,
406,
397,
390,
382,
371,
361,
353,
342,
332,
319,
310,
300,
290,
281,
273,
266,
255,
249,
240,
234,
225,
219,
213,
204,
195,
191,
185,
175,
169,
164,
157,
150,
142,
135,
130,
124,
119,
113,
106,
102,
98,
95,
93,
93,
100,
107,
119,
136,
160,
186,
218,
252,
291,
330,
369,
409,
450,
489,
527,
563,
596,
626,
657,
684,
709,
732,
748,
766,
782,
795,
805,
817,
824,
832,
837,
841,
841,
841,
842,
840,
836,
832,
829,
820,
814,
805,
794,
782,
770,
758,
749,
735,
724,
710,
700,
686,
675,
663,
652,
640,
628,
618,
605,
596,
582,
574,
562,
550,
539,
528,
517,
505,
496,
485,
475,
466,
457,
447,
438,
427,
419,
408,
399,
390,
381,
372,
361,
351,
341,
333,
324,
317,
308,
299,
289,
286,
277,
269,
262,
256,
247,
241,
233,
227,
219,
213,
205,
196,
184,
176,
169,
160,
152,
143,
136,
128,
119,
111,
103,
95,
89,
82,
76,
72,
72,
73,
80,
92,
106,
127,
150,
179,
214,
248,
284,
322,
360,
399,
436,
473,
508,
542,
571,
599,
627,
652,
675,
696,
716,
729,
744,
758,
769,
779,
787,
795,
800,
804,
808,
810,
812,
810,
807,
805,
801,
796,
789,
783,
773,
761,
751,
739,
730,
718,
708,
697,
685,
673,
661,
651,
639,
629,
618,
609,
598,
588,
581,
573,
564,
553,
546,
537,
531,
523,
516,
508,
501,
491,
483,
474,
465,
455,
446,
436,
424,
415,
405,
394,
384,
372,
362,
351,
341,
333,
323,
315,
306,
298,
291,
284,
276,
269])

ppg = np.array(list(map(np.float, ppg)))


