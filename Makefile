PART ?= 2021/01/part_1.py
INPUT ?= 2021/01/input

run: test
	@python $(PART) $(INPUT)

test:
	@python -m doctest $(PART)
