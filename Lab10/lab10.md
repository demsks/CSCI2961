Pull request was made succesfully. 
Below you will find the commands I used to alter the data for the lab part 3.


> use csci2963
switched to db csci2963
> db
csci2963
> db.definitions
csci2963.definitions
> db.definitions.find()
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8b9"), "definition" : " n. Solar Collector on top of the Science Center. Also known as the Laser Cannon.", "word" : "Alien Death Ray" }
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8b8"), "definition" : " n. Assemblage of Computer Maniacs, a group of wanted criminals at the VCC.", "word" : "ACM" }
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8b7"), "definition" : " exp. Equivalent to ``gag.''", "word" : "Ack" }
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8bb"), "definition" : " n. (RPI) A peculiar ethereal atmosphere indigenous to RPI, generated by the individual students' lack of concern for the events of the Real World. It works in inverse proportion to distance away from Troy and in direct proportion to the distance to Home, i.e., when you return to the nest you care once again. However, it also has hysterical properties and takes a certain amount of time to wear off.", "word" : "Apathy Field" }
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8be"), "definition" : " n.  Bullshit. No, really. Symbolized by the ``Right Hand Rule,'' see Halliday and Resnick for the formal definition.", "word" : "B-Vector" }
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8bd"), "definition" : " n. Something that can be put anywhere for any reason and not harmfully affect the outcome of any given event. See Fudge Factor.", "word" : "Arbitrary Constant" }
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8bc"), "definition" : " n. (RPI) The decaying ruins of the old Rensselaer gateway from Troy.", "word" : "Approach" }
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8bf"), "definition" : " n., acronym. (RPI) Burdett Avenue Resident Housing, the only REAL co-ed dorm on campus with its own bad version of DAKA. This place has a history of being a wild party dorm, thanks to the non-homogeneous population. Originally called the Burdett Avenue Residence Facility (BARF).", "word" : "BARH" }
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8c0"), "definition" : " adv. In discrete lumps.", "word" : "Batch" }
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8c2"), "definition" : " exp. (RPI) A more serious version of alarm, not to be confused with ``Be Like A Real Man.''", "word" : "Blarm" }
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8c3"), "definition" : " v. To be forced off MTS by the operator, owing to some ``fatal'' computer error.", "word" : "Blast" }
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8c4"), "definition" : " exp. A sound of disgust. --- adj.  --- blecherous.  To be disgusting. Also spelled ``Bletch'' and ``Bletcherous.''", "word" : "Blech" }
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8c1"), "definition" : " n. A main staple of the Rensselaer Diet.", "word" : "Beer" }
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8c5"), "definition" : " v. To lose big, or fail miserably.", "word" : "Blow Away" }
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8c6"), "definition" : " v. To disregard; see Punt.", "word" : "Blow Off" }
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8c7"), "definition" : " n. A very random and unpredictable sort of motion. Best typified by, say, a nice hot cup of tea. (Also see Halliday and Resnick.)", "word" : "Brownian Motion" }
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8c8"), "definition" : " n. Your first degree, assuming you finish.", "word" : "B.S." }
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8c9"), "definition" : " n. The Center for Industrial Innovation, or CII, as translated by lovers of Roman numerals.", "word" : "Building 102" }
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8cc"), "definition" : " n.  A package containing munchies, junk food and probably a stuffed animal, intended to ease homesickness.", "word" : "Care Package" }
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8ca"), "definition" : " v. To erase, eradicate or otherwise remove from the face of the Earth.", "word" : "Bulk" }
Type "it" for more
> 
> 
> 
> 
> db.definitions.findOne()
{
	"_id" : ObjectId("56fe9e22bad6b23cde07b8b9"),
	"definition" : " n. Solar Collector on top of the Science Center. Also known as the Laser Cannon.",
	"word" : "Alien Death Ray"
} 
> db.definitions.findOne()
{
	"_id" : ObjectId("56fe9e22bad6b23cde07b8b9"),
	"definition" : " n. Solar Collector on top of the Science Center. Also known as the Laser Cannon.",
	"word" : "Alien Death Ray"
}
> db.definitions.find({word: "Capitaland"})
{ "_id" : ObjectId("56fe9e22bad6b23cde07b8cb"), "definition" : " n. (RPI) For those who don't listen to WPYX, and still don't know this term, it means Albany and Rensselaer Counties and the general surrounding area.", "word" : "Capitaland" }
> 
> db.definitions.find({word: "Recursive"})
{ "_id" : ObjectId("56fe9e22bad6b23cde07b923"), "definition" : " adj. See recursive.", "word" : "Recursive" }
> 
> 
> 
> db.definitions.find({{_id: ObjectId("56fe9e22bad6b23cde07b923")
... }

> db.definitions.find({{_id: ObjectId("56fe9e22bad6b23cde07b923")]
2016-11-15T12:54:34.488-0500 E QUERY    [thread1] SyntaxError: invalid property id @(shell):1:21
> 
> 
> db.definitions.find({{_id: ObjectId("56fe9e22bad6b23cde07b923")})
... db.definitions.find({{_id: ObjectId("56fe9e22bad6b23cde07b923")]^C

> 
> db.definitions.find({_id: ObjectId("56fe9e22bad6b23cde07b923")})
{ "_id" : ObjectId("56fe9e22bad6b23cde07b923"), "definition" : " adj. See recursive.", "word" : "Recursive" }
> 
> 
> db.definitions.insert({word: objective, definition:something that you are trying to achieve})
2016-11-15T13:00:19.801-0500 E QUERY    [thread1] SyntaxError: missing } after property list @(shell):1:61

> db.definitions.insert({word: Objective, definition:"something that you are trying to achieve"})
2016-11-15T13:00:45.105-0500 E QUERY    [thread1] ReferenceError: Objective is not defined :
@(shell):1:24

> db.definitions.insert({word: "Objective", definition:"something that you are trying to achieve"})
WriteResult({ "nInserted" : 1 })
> db.definitions.update({query}, {new document})
2016-11-15T13:01:44.274-0500 E QUERY    [thread1] SyntaxError: missing : after property id @(shell):1:36

> db.definitions.update({ query }, { new document })
2016-11-15T13:02:21.119-0500 E QUERY    [thread1] SyntaxError: missing : after property id @(shell):1:39

> 
> 
> 
> db.definitions.insert({word: "Objective", definition:"something that you are trying to achieve"})
WriteResult({ "nInserted" : 1 })
> 
> 
> 
> db.definitions.find({word: "Objective"})
{ "_id" : ObjectId("582b4d5aa4f7bec2b77b8250"), "word" : "Objective", "definition" : "something that you are trying to achieve" }
{ "_id" : ObjectId("582b4ea2a4f7bec2b77b8251"), "word" : "Objective", "definition" : "something that you are trying to achieve" }
> db.definitions.update({ word: "Objective" }, { newDB })
2016-11-15T13:09:52.877-0500 E QUERY    [thread1] ReferenceError: newDB is not defined :
@(shell):1:48

> mongoexport --host=127.0.0.1 --db csci2963 --collection definitions --out definitions.json

> 
> 
> db.definitions.drop()
true