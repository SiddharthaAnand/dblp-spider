# dblp-spider
 Collection of co-authorship network from http://dblp.uni-trier.de/. The site stores
 information about the author who have worked together on a research topic. You can
 visit the website and check it out for more information about the kind of data
 that is present there.

# Example of a co-authorship network
```
"Siddhartha Anand" "Partha Basuchowdhuri"
"Siddhartha Anand" "Khusbu Mishra"
...
```
The above example denotes an edge-list (author_one->author_two). Such an edge-list
denotes a graph of co-authors who have worked on a paper together. The file being
generated when you run the command is in json format.

# What does this code do ?
The code here, crawls the website of dblp, collects coauthors name list, their communities
to which they belong, articles that they have published together. You can modify it extract
even more information from the web page.

# How to clone the repository
Simply, run the following command:
```
>>> git clone https://github.com/SiddharthaAnand/dblp-spider.git
```
This will clone this repository to your local system. 

# How to run the code
Make sure you are in the directory of dblp-spider. Run the following command:
```
>>> scrapy crawl dblpspider [-o] [filename]
```

This will start the spider, send requests asynchronously and receive data and store the
output (denoted by '-o' in the filename given by you.

For example:
```
>>> scrapy crawl dblpspider -o dblp_data.jl
```

# Sample json data
This is the sample data that you might get after the crawl is over.
```
>>> head dblp_json.jl
{"coauthors_name_list": ["Siddhartha Anand", "Partha Basuchowdhuri", "Subhashis Majumder", "Sanjoy Kumar Saha", "Diksha Roy Srivastava"], "coauthor_communities_list": ["show coauthor community: group 1", "show coauthor community: group 1", "show coauthor community: group 1", "show coauthor community: group 1", "show coauthor community: group 1"], "author_name": "Riya Roy", "author_articles_published": ["Spanning tree-based fast community detection methods in social networks."]}
{"coauthors_name_list": ["Partha Basuchowdhuri", "Subhashis Majumder", "V. K. Lakshan Prabhu", "Sanjoy Kumar Saha"], "coauthor_communities_list": ["show coauthor community: group 1", "show coauthor community: group 1", "show coauthor community: group 1", "show coauthor community: group 1"], "author_name": "Mithun Roy", "author_articles_published": ["Unified scheme for finding disjoint and overlapping communities in social networks using strength of ties."]}
{"coauthors_name_list": ["Partha Basuchowdhuri", "Subhashis Majumder", "Mithun Roy", "Sanjoy Kumar Saha"], "coauthor_communities_list": ["show coauthor community: group 1", "show coauthor community: group 1", "show coauthor community: group 1", "show coauthor community: group 1"], "author_name": "V. K. Lakshan Prabhu", "author_articles_published": ["Unified scheme for finding disjoint and overlapping communities in social networks using strength of ties."]}
...
```

# Authors
* [Khusbu Mishra](https://github.com/Khusbu)
* [Siddhartha Anand](https://github.com/SiddharthaAnand)

# Future enhancements
* Add a no-sql db to insert data 
* Deploy the spider on a server for large scale crawl
* Extract more data from dblp
* Visualize the data using a visualization tool
