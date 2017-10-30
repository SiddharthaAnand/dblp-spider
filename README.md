# dblp-spider

A spider written using [scrapy](https://scrapy.org/) that crawls [dblp](http://dblp.uni-trier.de/) website to
extract various data about the authors like his/her co-authors' names, communities to which he/she belongs to and
articles that he/she has published. It is then used to build a co-authorship network graph.

### Example of a co-authorship network
```
"Siddhartha Anand" "Partha Basuchowdhuri"
"Siddhartha Anand" "Khusbu Mishra"
...
```
The above example denotes an edge-list (author_one->author_two). Such an edge-list
denotes a graph of co-authors who have worked on a paper together.

## Dependencies

- [scrapy](https://doc.scrapy.org/en/latest/intro/install.html)
- [python 2.7](https://www.python.org/)

## How to clone the repository
Simply, run the following command:
```
$ git clone https://github.com/SiddharthaAnand/dblp-spider.git
```
This will clone this repository to your local system.

## How to run the code
Make sure you are in the working directory of dblp-spider. Then run the following command:
```
$ scrapy crawl dblpspider [-o] [filename]
```

This will start the spider, send requests asynchronously and receive data and store the
output (denoted by '-o' in the filename given by you).

For example:
```
$ scrapy crawl dblpspider -o dblp_data.jl
```

### Sample json data
This is the sample data that you might get after the crawl is over.
You can optionally use the [in-built json package](https://docs.python.org/2/library/json.html) to pretty print the
contents of the json file.
```
$ head dblp_json.jl
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

## Licence
This project is licensed under Apache Licence - see the [LICENSE.md](/LICENSE.md) for more details.

## Future enhancements
* Add a no-sql db to insert data
* Deploy the spider on a server for large scale crawl
* Extract more data from dblp
* Visualize the data using a visualization tool

## Contributions
Any kind of contribution or suggestion are always welcome. You can modify it and extract even more data from [dblp](http://dblp.uni-trier.de/).
