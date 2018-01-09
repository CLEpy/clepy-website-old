# clepy-website

Source for the clepy.org website

The site is built using [pelican](http://docs.getpelican.com/en/stable/) (a 
static site generator) on Python 3.

## Getting Started

* Fork this repo
* Clone your fork
* Install the requirements (it's recommended you use a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/))

```sh
pip install requirements.in
```
* Generate the website output

```sh
pelican content
```

* Run the development server

```sh
./develop_server.sh start
```

* Navigate to the local site at [http://localhost:8000](http://localhost:8000)

## Contributing

Fork the repo and submit a pull request. 

Some key notes on forks and pull requests:

* [Creating a pull request from a fork](https://help.github.com/articles/creating-a-pull-request-from-a-fork/)
* [Setting up origin on a fork](https://help.github.com/articles/configuring-a-remote-for-a-fork/)
* [Syncing a fork](https://help.github.com/articles/syncing-a-fork/)
