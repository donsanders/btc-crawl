Build & Run:
make && ./analyzenetwork.sh

After 100+ minutes depending on system performance the script should print YES if a small-world graph has been detected. Otherwise it will crash or print NO.

The following dependencies are required on OS X:

#Brew:
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

#Brew recipes:
brew install python3
brew install go
brew install coreutils
brew install pkg-config
brew install gnu-sed

#Go modules:
go get github.com/alexcesaro/log
go get github.com/alexcesaro/golog
go get github.com/btcsuite/btcd/chaincfg
go get github.com/btcsuite/btcd/wire
go get github.com/jessevdk/go-flags

#Pips
sudo easy_install pip

#Networkx
pip install networkx

README for btc-crawl follows. The btc-crawl authors wrote all the network code. I’m just piggybacking on their project and go. To save time and because I’m researching go.

# btc-crawl

Bitcoin node network crawler (written in golang).

This is a for-fun project to explore the Bitcoin protocol and network.

Current status: 
* JSON streaming is in place, and graceful shutdown.
* ~~It crawls with all kinds of nice parameters but stores everything in memory
  until dumping a giant JSON blob at the end.~~
* ~~It crawls from hard-coded values and spits a bunch of stuff to
stdout.~~


## Usage

```
$ go get github.com/shazow/btc-crawl
$ btc-crawl --help
...
$ btc-crawl \
  --concurrency=100 \
  --output="btc-crawl.json" \
  --peer-age="24h" \
  --user-agent="/batman:1.0/" \
  --verbose
...
```

**Estimated crawl time:** Unknown.

There should be under 10,000 active network nodes at any given time, according
to [bitnodes.io](https://getaddr.bitnodes.io/). Each node returns around ~2,500
known nodes, but usually only several have timestamps within the last hour.


## Todo

(In approximate order of priority)

* Namespace useful sub-packages properly (outside of `main`)
* Fix `go build -race` race condition warnings. (Not sure if this is feasible. `golog` and other
  fundamental pieces seem to trigger warnings possibly erroneously.)
* Tests would be nice.


## License

MIT (see LICENSE file).
