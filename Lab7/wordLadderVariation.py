''' Shane Demskie CSCI 2961 Lab 7''' 

"""
SGBWords() returns an undirected graph over the 5757 5-letter
words in the datafile words_dat.txt.  Two words are connected by an edge
if they differ in one letter, resulting in 14,135 edges. This example
is described in Section 1.1 in Knuth's book [1,2].
References.
----------
[1] Donald E. Knuth,
    "The Stanford GraphBase: A Platform for Combinatorial Computing",
    ACM Press, New York, 1993.
[2] http://www-cs-faculty.stanford.edu/~knuth/sgb.html
"""

__author__ = """Brendt Wohlberg\nAric Hagberg (hagberg@lanl.gov)"""
__date__ = "$Date: 2005-04-01 07:56:04 -0700 (Fri, 01 Apr 2005) $"
__credits__ = """"""
__revision__ = ""



from networkx import *
import re
import sys

__author__ = """"""
__date__ = ""
__credits__ = """"""
__version__ = ""
# $Header$


def _notComment(line):
    return not(line.startswith('*'))


def _wdist(a,b):
    d=abs(len(a)-len(b))
    
    for k in range(0,len(a)):
        found = False
        if (len(b)) > 0:
            for n in range(0,len(b)):
                if a[k] == b[n]:
                    found = True
                    b = b.replace(b[n], "")
                    break
            if found == False:
                d = d+1
    return d


def words_graph():
    """ Return example graph from the Stanford GraphBase"""

    import sys
    # open file words_dat.txt.gz
    try:
        try:
            import gzip
            fh=gzip.open('words_dat.txt.gz','r')
        except:
            fh=open("words_dat.txt","r")
    except IOError:
        raise "File words_dat.txt not found."

    G = Graph(name="words")
    sys.stderr.write("Loading words_dat.txt: ")
    for line in fh.readlines():
        if line.startswith("*"):
            continue
        w=line[0:5]
        G.add_node(w)
    nwords=number_of_nodes(G)
    words=G.nodes()
    for k in xrange(0,nwords):
        if (k%100==0):
            sys.stderr.softspace=0
            sys.stderr.write(".")
        for l in xrange(k+1,nwords):
            if _wdist(words[k],words[l]) == 1:
                if words[k] == "chaos" and words[l] == "shoes":
                    print "THEIS"
                    break
                G.add_edge(words[k],words[l])
    return G


if __name__ == '__main__':
    from networkx import *
    G=words_graph()

    print "Loaded words_dat.txt containing 5757 five-letter English words."
    print "Two words are connected if they differ in one letter."
    print "graph has %d nodes with %d edges"\
          %(number_of_nodes(G),number_of_edges(G))

    sp=shortest_path(G, 'chaos', 'order')
    print "shortest path between 'chaos' and 'order' is:\n", sp

    print
    sp=shortest_path(G, 'nodes', 'graph')
    print "shortest path between 'nodes' and 'graph' is:\n", sp

    print
    sp=shortest_path(G, 'moron', 'smart')
    print "shortest path between 'moron' and 'smart' is:\n", sp

    print
    sp=shortest_path(G, 'pound', 'marks')
    print "shortest path between 'pound' and 'marks' is:\n", sp