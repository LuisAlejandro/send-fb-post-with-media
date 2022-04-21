#!/usr/bin/env make -f
# -*- makefile -*-

SHELL = bash -e

BASEDIR = $(shell pwd)


image:
	@docker-compose -p send-fb-post-with-media -f docker-compose.yml build \
		--force-rm --pull

start:
	@docker-compose -p send-fb-post-with-media -f docker-compose.yml up \
		--remove-orphans -d

console: start
	@docker-compose -p send-fb-post-with-media -f docker-compose.yml exec \
		--user luisalejandro send-fb-post-with-media bash

publish: start
	@docker-compose -p send-fb-post-with-media -f docker-compose.yml exec \
		--user luisalejandro send-fb-post-with-media python3 entrypoint.py

stop:
	@docker-compose -p send-fb-post-with-media -f docker-compose.yml stop

down:
	@docker-compose -p send-fb-post-with-media -f docker-compose.yml down \
		--remove-orphans

destroy:
	@docker-compose -p send-fb-post-with-media -f docker-compose.yml down \
		--rmi all --remove-orphans -v

virtualenv: start
	@docker-compose -p send-fb-post-with-media -f docker-compose.yml exec \
		--user luisalejandro send-fb-post-with-media python3 -m venv --clear --copies ./virtualenv
	@docker-compose -p send-fb-post-with-media -f docker-compose.yml exec \
		--user luisalejandro send-fb-post-with-media ./virtualenv/bin/pip install -U wheel setuptools
	@docker-compose -p send-fb-post-with-media -f docker-compose.yml exec \
		--user luisalejandro send-fb-post-with-media ./virtualenv/bin/pip install -r requirements.txt -r requirements-dev.txt
