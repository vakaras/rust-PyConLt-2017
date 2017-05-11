test: env
	env/bin/test

fresh: clean env
	env/bin/test

env: .virtualenv
	python3 .virtualenv/source/virtualenv.py env
	env/bin/pip install setuptools-rust
	env/bin/pip install -e ../tmrs
	env/bin/pip install ipdb
	env/bin/pip install -e ../tmpy
	env/bin/pip install -e .

.virtualenv:
	mkdir -p .virtualenv
	wget -c \
		https://pypi.python.org/packages/d4/0c/9840c08189e030873387a73b90ada981885010dd9aea134d6de30cd24cb8/virtualenv-15.1.0.tar.gz \
		-O .virtualenv/archive.tar.gz
	tar -xvf .virtualenv/archive.tar.gz
	mv virtualenv-* .virtualenv/source

clean:
	rm -rf env
