1. Read chapter 9 and/or review slides given	-- **Completed**
2. Read on the background of Association Rule Mining and install the two packages listed.	-- **Completed**
3. Implement an Association rule for the Graduate Admissions Data Set given
	* **See below for code and screen captures of examples**
	
4. Try Different Visualizations shown in Chapter 9 of the book	-- **Completed**
5. Optional: Take the course listed in the lab	-- **Completed**
6. Write a paragraph description of the status of your project - What did you do last week on your project? 	-- **Completed**
	* **What I've done**: I went through the code and looked at existing comments / notes throughout. Additionally, I reached out to the original creator and plan on reaching out to the 4 students who worked on the project last semester. 
	* **Status of my project**: I have never worked with a web project before, so I am taking this project as an opportunity to now only extend on an existing project which I will use in the future, but to also learn about web programming paradigms and developement. 




---Code used to implement the R association rules---
rules.all <- apriori(admissions)
inspect(rules.all)
rules <- apriori(admissions, control = list(verbose=F),
                 parameter = list(minlen=2, supp=0.005, conf=0.8),
                 appearance = list(rhs=c("admit=0", "admit=1"),
                                   default="lhs"))
quality(rules) <- round(quality(rules), digits=3)
rules.sorted <- sort(rules, by="lift")
inspect(rules.sorted)

rules.all <- apriori(admissions)
inspect(rules.all)
rules <- apriori(admissions, control = list(verbose=F),
                 parameter = list(minlen=2, supp=0.005, conf=0.8),
                 appearance = list(rhs=c("rank=4", "rank=2"),
                                   default="lhs"))
quality(rules) <- round(quality(rules), digits=3)
rules.sorted <- sort(rules, by="lift")
inspect(rules.sorted)

---OUTPUT 1---
1   {gpa=3.71}                => {admit=1} 0.005   1.000      3.150
19  {gpa=3.56}                => {admit=1} 0.008   1.000      3.150
53  {gre=700,gpa=3.56}        => {admit=1} 0.005   1.000      3.150
54  {gpa=3.56,rank=2}         => {admit=1} 0.005   1.000      3.150
56  {gre=620,gpa=3.37}        => {admit=1} 0.005   1.000      3.150
57  {gpa=3.6,rank=3}          => {admit=1} 0.005   1.000      3.150
59  {gpa=3.81,rank=1}         => {admit=1} 0.005   1.000      3.150
64  {gpa=3,rank=2}            => {admit=1} 0.005   1.000      3.150
72  {gre=520,gpa=3.74}        => {admit=1} 0.005   1.000      3.150
76  {gpa=3.58,rank=1}         => {admit=1} 0.008   1.000      3.150
79  {gre=460,gpa=3.64}        => {admit=1} 0.005   1.000      3.150
80  {gpa=3.64,rank=1}         => {admit=1} 0.005   1.000      3.150
81  {gre=540,gpa=3.49}        => {admit=1} 0.005   1.000      3.150
82  {gre=620,gpa=3.95}        => {admit=1} 0.005   1.000      3.150
83  {gpa=3.95,rank=3}         => {admit=1} 0.005   1.000      3.150
84  {gpa=3.95,rank=2}         => {admit=1} 0.005   1.000      3.150
89  {gre=780,rank=2}          => {admit=1} 0.005   1.000      3.150
92  {gre=760,rank=1}          => {admit=1} 0.005   1.000      3.150
93  {gre=760,rank=2}          => {admit=1} 0.005   1.000      3.150
97  {gpa=3.46,rank=2}         => {admit=1} 0.005   1.000      3.150
120 {gre=740,rank=2}          => {admit=1} 0.005   1.000      3.150
132 {gre=520,gpa=4}           => {admit=1} 0.005   1.000      3.150
145 {gre=620,gpa=3.95,rank=3} => {admit=1} 0.005   1.000      3.150
146 {gre=800,gpa=4,rank=3}    => {admit=1} 0.005   1.000      3.150
29  {gpa=3.64}                => {admit=1} 0.010   0.800      2.520
30  {gpa=3.95}                => {admit=1} 0.010   0.800      2.520
34  {gre=780}                 => {admit=1} 0.010   0.800      2.520
36  {gre=760}                 => {admit=1} 0.010   0.800      2.520
133 {gre=800,gpa=4}           => {admit=1} 0.010   0.800      2.520
141 {gre=620,rank=1}          => {admit=1} 0.010   0.800      2.520
2   {gpa=2.82}                => {admit=0} 0.005   1.000      1.465
3   {gpa=2.78}                => {admit=0} 0.005   1.000      1.465
4   {gpa=3.29}                => {admit=0} 0.005   1.000      1.465
5   {gpa=3.25}                => {admit=0} 0.005   1.000      1.465
6   {gpa=3.04}                => {admit=0} 0.005   1.000      1.465
7   {gpa=3.16}                => {admit=0} 0.005   1.000      1.465
8   {gpa=3.62}                => {admit=0} 0.005   1.000      1.465
9   {gpa=3.73}                => {admit=0} 0.005   1.000      1.465
10  {gpa=2.92}                => {admit=0} 0.005   1.000      1.465
11  {gpa=2.71}                => {admit=0} 0.005   1.000      1.465
12  {gpa=2.88}                => {admit=0} 0.005   1.000      1.465
13  {gpa=2.85}                => {admit=0} 0.005   1.000      1.465
14  {gpa=2.79}                => {admit=0} 0.005   1.000      1.465
15  {gpa=3.01}                => {admit=0} 0.005   1.000      1.465
16  {gpa=3.24}                => {admit=0} 0.005   1.000      1.465
17  {gpa=2.7}                 => {admit=0} 0.005   1.000      1.465
18  {gpa=3.92}                => {admit=0} 0.005   1.000      1.465
20  {gpa=3.57}                => {admit=0} 0.008   1.000      1.465
21  {gpa=3.28}                => {admit=0} 0.010   1.000      1.465
22  {gre=360}                 => {admit=0} 0.010   1.000      1.465
23  {gpa=3.07}                => {admit=0} 0.010   1.000      1.465
24  {gpa=2.9}                 => {admit=0} 0.010   1.000      1.465
25  {gpa=3.08}                => {admit=0} 0.010   1.000      1.465
27  {gpa=3.51}                => {admit=0} 0.012   1.000      1.465
32  {gpa=3.33}                => {admit=0} 0.012   1.000      1.465
35  {gpa=2.93}                => {admit=0} 0.012   1.000      1.465
38  {gpa=3.34}                => {admit=0} 0.012   1.000      1.465
40  {gre=420}                 => {admit=0} 0.018   1.000      1.465
41  {gpa=3.4}                 => {admit=0} 0.018   1.000      1.465
43  {gre=380}                 => {admit=0} 0.020   1.000      1.465
44  {gpa=3.31}                => {admit=0} 0.020   1.000      1.465
49  {gre=600,gpa=2.82}        => {admit=0} 0.005   1.000      1.465
50  {gpa=2.82,rank=4}         => {admit=0} 0.005   1.000      1.465
51  {gpa=2.88,rank=2}         => {admit=0} 0.005   1.000      1.465
52  {gpa=3.24,rank=4}         => {admit=0} 0.005   1.000      1.465
55  {gpa=3.57,rank=3}         => {admit=0} 0.005   1.000      1.465
58  {gpa=2.81,rank=3}         => {admit=0} 0.005   1.000      1.465
60  {gpa=3.61,rank=3}         => {admit=0} 0.005   1.000      1.465
61  {gpa=3.5,rank=2}          => {admit=0} 0.008   1.000      1.465
62  {gre=700,gpa=3.65}        => {admit=0} 0.005   1.000      1.465
63  {gpa=3.65,rank=2}         => {admit=0} 0.008   1.000      1.465
65  {gre=540,gpa=3.28}        => {admit=0} 0.005   1.000      1.465
66  {gpa=3.28,rank=1}         => {admit=0} 0.005   1.000      1.465
67  {gpa=3.28,rank=3}         => {admit=0} 0.005   1.000      1.465
68  {gre=360,rank=3}          => {admit=0} 0.008   1.000      1.465
69  {gpa=3.36,rank=2}         => {admit=0} 0.005   1.000      1.465
70  {gpa=3.07,rank=2}         => {admit=0} 0.008   1.000      1.465
71  {gre=340,rank=3}          => {admit=0} 0.005   1.000      1.465
73  {gpa=3.08,rank=2}         => {admit=0} 0.005   1.000      1.465
74  {gpa=3.38,rank=2}         => {admit=0} 0.005   1.000      1.465
75  {gpa=3.51,rank=2}         => {admit=0} 0.010   1.000      1.465
77  {gpa=3.58,rank=2}         => {admit=0} 0.005   1.000      1.465
78  {gpa=3.43,rank=3}         => {admit=0} 0.008   1.000      1.465
85  {gpa=3.94,rank=3}         => {admit=0} 0.005   1.000      1.465
86  {gpa=3.33,rank=4}         => {admit=0} 0.005   1.000      1.465
87  {gpa=3.33,rank=3}         => {admit=0} 0.005   1.000      1.465
88  {gpa=3.77,rank=3}         => {admit=0} 0.008   1.000      1.465
90  {gpa=2.93,rank=4}         => {admit=0} 0.005   1.000      1.465
91  {gpa=2.93,rank=3}         => {admit=0} 0.005   1.000      1.465
94  {gpa=3.34,rank=3}         => {admit=0} 0.005   1.000      1.465
95  {gpa=3.34,rank=2}         => {admit=0} 0.005   1.000      1.465
96  {gpa=3.46,rank=4}         => {admit=0} 0.005   1.000      1.465
98  {gre=620,gpa=3.63}        => {admit=0} 0.005   1.000      1.465
99  {gpa=3.63,rank=3}         => {admit=0} 0.005   1.000      1.465
100 {gpa=2.98,rank=3}         => {admit=0} 0.005   1.000      1.465
101 {gpa=3.15,rank=4}         => {admit=0} 0.005   1.000      1.465
102 {gpa=3.15,rank=3}         => {admit=0} 0.005   1.000      1.465
103 {gre=420,rank=1}          => {admit=0} 0.005   1.000      1.465
104 {gre=420,rank=4}          => {admit=0} 0.008   1.000      1.465
105 {gpa=3.45,rank=4}         => {admit=0} 0.005   1.000      1.465
106 {gre=580,gpa=3.4}         => {admit=0} 0.008   1.000      1.465
107 {gpa=3.4,rank=3}          => {admit=0} 0.008   1.000      1.465
108 {gpa=3.4,rank=2}          => {admit=0} 0.008   1.000      1.465
109 {gpa=3.35,rank=3}         => {admit=0} 0.010   1.000      1.465
110 {gre=380,rank=4}          => {admit=0} 0.008   1.000      1.465
111 {gre=380,rank=3}          => {admit=0} 0.010   1.000      1.465
112 {gpa=3.31,rank=1}         => {admit=0} 0.005   1.000      1.465
113 {gpa=3.31,rank=4}         => {admit=0} 0.005   1.000      1.465
114 {gpa=3.31,rank=3}         => {admit=0} 0.008   1.000      1.465
115 {gre=440,rank=4}          => {admit=0} 0.008   1.000      1.465
116 {gre=400,rank=3}          => {admit=0} 0.010   1.000      1.465
118 {gre=740,rank=1}          => {admit=0} 0.005   1.000      1.465
122 {gre=460,rank=2}          => {admit=0} 0.012   1.000      1.465
123 {gre=480,rank=3}          => {admit=0} 0.005   1.000      1.465
124 {gre=640,rank=3}          => {admit=0} 0.020   1.000      1.465
125 {gre=500,rank=4}          => {admit=0} 0.022   1.000      1.465
127 {gre=700,rank=3}          => {admit=0} 0.008   1.000      1.465
129 {gre=600,rank=4}          => {admit=0} 0.008   1.000      1.465
130 {gre=560,rank=4}          => {admit=0} 0.010   1.000      1.465
131 {gre=660,rank=1}          => {admit=0} 0.005   1.000      1.465
134 {gre=800,rank=4}          => {admit=0} 0.005   1.000      1.465
137 {gre=580,gpa=4}           => {admit=0} 0.008   1.000      1.465
142 {gre=620,rank=4}          => {admit=0} 0.008   1.000      1.465
143 {gre=600,gpa=2.82,rank=4} => {admit=0} 0.005   1.000      1.465
144 {gre=700,gpa=3.65,rank=2} => {admit=0} 0.005   1.000      1.465
128 {gre=700,rank=2}          => {admit=0} 0.028   0.917      1.343
47  {gre=500}                 => {admit=0} 0.048   0.905      1.326
126 {gre=500,rank=3}          => {admit=0} 0.020   0.889      1.302
42  {gpa=3.35}                => {admit=0} 0.015   0.857      1.256
121 {gre=720,rank=3}          => {admit=0} 0.015   0.857      1.256
117 {gre=400,rank=2}          => {admit=0} 0.012   0.833      1.221
136 {gre=540,rank=3}          => {admit=0} 0.012   0.833      1.221
48  {rank=4}                  => {admit=0} 0.138   0.821      1.203
46  {gre=400}                 => {admit=0} 0.022   0.818      1.199
26  {gpa=3.38}                => {admit=0} 0.010   0.800      1.172
28  {gpa=3.43}                => {admit=0} 0.010   0.800      1.172
31  {gpa=3.94}                => {admit=0} 0.010   0.800      1.172
33  {gpa=3.77}                => {admit=0} 0.010   0.800      1.172
37  {gpa=3.59}                => {admit=0} 0.010   0.800      1.172
39  {gpa=3.13}                => {admit=0} 0.010   0.800      1.172
45  {gre=440}                 => {admit=0} 0.020   0.800      1.172
119 {gre=740,rank=4}          => {admit=0} 0.010   0.800      1.172
135 {gre=540,rank=4}          => {admit=0} 0.010   0.800      1.172
138 {gre=580,rank=4}          => {admit=0} 0.010   0.800      1.172
139 {gre=580,rank=3}          => {admit=0} 0.010   0.800      1.172
140 {gre=580,rank=2}          => {admit=0} 0.030   0.800      1.172

---OUTPUT 2---
1  {gpa=3.24}                 => {rank=4} 0.005   1.0        5.970
3  {gpa=2.82}                 => {rank=4} 0.005   1.0        5.970
5  {gpa=2.86}                 => {rank=4} 0.005   1.0        5.970
10 {admit=0,gpa=3.24}         => {rank=4} 0.005   1.0        5.970
11 {gre=600,gpa=2.82}         => {rank=4} 0.005   1.0        5.970
12 {admit=0,gpa=2.82}         => {rank=4} 0.005   1.0        5.970
17 {admit=1,gpa=3.52}         => {rank=4} 0.005   1.0        5.970
26 {admit=0,gre=600,gpa=2.82} => {rank=4} 0.005   1.0        5.970
2  {gpa=3.75}                 => {rank=2} 0.005   1.0        2.649
4  {gpa=2.88}                 => {rank=2} 0.005   1.0        2.649
6  {gpa=2.62}                 => {rank=2} 0.005   1.0        2.649
7  {gpa=3.05}                 => {rank=2} 0.008   1.0        2.649
13 {admit=0,gpa=2.88}         => {rank=2} 0.005   1.0        2.649
14 {admit=0,gpa=3.05}         => {rank=2} 0.005   1.0        2.649
15 {gre=700,gpa=3.65}         => {rank=2} 0.005   1.0        2.649
16 {admit=0,gpa=3.65}         => {rank=2} 0.008   1.0        2.649
18 {admit=0,gpa=3.5}          => {rank=2} 0.008   1.0        2.649
19 {admit=0,gpa=3.58}         => {rank=2} 0.005   1.0        2.649
20 {gre=660,gpa=3.49}         => {rank=2} 0.005   1.0        2.649
22 {admit=1,gpa=3.46}         => {rank=2} 0.005   1.0        2.649
23 {gre=560,gpa=3.59}         => {rank=2} 0.005   1.0        2.649
24 {admit=1,gpa=3.15}         => {rank=2} 0.005   1.0        2.649
25 {admit=1,gre=440}          => {rank=2} 0.005   1.0        2.649
27 {admit=0,gre=700,gpa=3.65} => {rank=2} 0.005   1.0        2.649
8  {gpa=3.13}                 => {rank=2} 0.010   0.8        2.119
9  {gpa=3.51}                 => {rank=2} 0.010   0.8        2.119
21 {admit=0,gpa=3.51}         => {rank=2} 0.010   0.8        2.119

---Code used to plot the admissions data---

library(arulesViz)
plot(rules)
plot(rules, method="graph", control=list(type="items"))
plot(rules, method="paracoord", control=list(reorder=TRUE))

---Screen caps of the above plots---