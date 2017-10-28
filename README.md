# dblp-spider
 Collection of co-authorship network from http://dblp.uni-trier.de/. The site stores
 information about the author who have worked together on a research topic. You can
 visit the website and check it out for more information about the kind of data
 that is present there.

### Example of a co-authorship network
```
"Siddhartha Anand" "Partha Basuchowdhuri"
"Siddhartha Anand" "Khusbu Mishra"
...
```
The above example denotes an edge-list (author_one->author_two). Such an edge-list
denotes a graph of co-authors who have worked on a paper together. The file being
generated when you run the command is in json format.

## What does the spider do?
The code here, crawls the website of dblp, collects coauthors name list, their communities
to which they belong, articles that they have published together. You can modify it and extract
even more information from the web page.

## How to clone the repository
Simply, run the following command:
```
>>> git clone https://github.com/SiddharthaAnand/dblp-spider.git
```
This will clone this repository to your local system. 

## How to run the code
Make sure you are in the working directory of dblp-spider. The working directory looks like this:
```
>>> tree
|-- coauthornetwork
|   |-- __init__.py
|   |-- items.py
|   |-- middlewares.py
|   |-- pipelines.py
|   |-- settings.py
|   `-- spiders
|       |-- example.py
|       `-- __init__.py
|-- dblp_data1.jl
|-- dblp_data.jl
|-- LICENSE.md
|-- README.md
`-- scrapy.cfg
```
Run the following command:
```
>>> scrapy crawl dblpspider [-o] [filename]
```

This will start the spider, send requests asynchronously and receive data and store the
output (denoted by '-o' in the filename given by you.

For example:
```
>>> scrapy crawl dblpspider -o dblp_data.jl
```

### Sample json data
This is the sample data that you might get after the crawl is over.
You can optionally use the in-built json package to pretty print the
contents of the json file. You can google it to know how to use it.
```
>>> head dblp_json.jl
{
    "author_articles_published": [
        "Spanning tree-based fast community detection methods in social networks."
    ],
    "author_name": "Siddhartha Anand",
    "coauthor_communities_list": [
        "show coauthor community: group 1",
        "show coauthor community: group 1",
        "show coauthor community: group 1",
        "show coauthor community: group 1",
        "show coauthor community: group 1"
    ],
    "coauthors_name_list": [
        "Partha Basuchowdhuri",
        "Subhashis Majumder",
        "Riya Roy",
        "Sanjoy Kumar Saha",
        "Diksha Roy Srivastava"
    ]
}
...
```
## Authors
* [Khusbu Mishra](https://github.com/Khusbu)
* [Siddhartha Anand](https://github.com/SiddharthaAnand)

## Licence
This project is licensed under Apache Licence - see the [LICENSE.md](/LICENSE.md) for more details.
## Future enhancements
* Add a no-sql db to insert data 
* Deploy the spider on a server for large scale crawl
* Extract more data from dblp
* Visualize the data using a visualization tool
