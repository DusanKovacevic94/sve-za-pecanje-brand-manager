.PHONY: validate assets-check assets-sync test check

validate:
	python3 scripts/validate.py

assets-check:
	python3 scripts/sync_assets.py

assets-sync:
	python3 scripts/sync_assets.py --write

test:
	python3 -m unittest discover -s tests

check: validate test
