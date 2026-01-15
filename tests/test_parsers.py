# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    # Test edge cases
    # test if file is blank - raise Error
    with pytest.raises(ValueError):
        parser = FastaParser("tests/blank.fa")
        list(parser)
    # test if file is bad - raise Error
    with pytest.raises(ValueError):
        parser = FastaParser("tests/bad.fa")
        list(parser)
    # Test general cases (every seq has an actual sequence, total lines match)
    test_obj = FastaParser("data/test.fa")
    for record in test_obj:
        assert len(record) == 2  # Has 2 items
        assert record[0] is not None  # Header exists
        assert record[1] is not None  # Sequence exists
        assert len(record[0]) > 0  # Header is not empty
        assert len(record[1]) > 0  # Sequence is not empty
    #total length 200/2
    records = list(test_obj)
    assert len(records) == 100

def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in - if a fastq file is
    read, the first item is None
    """

    test_object = FastaParser("data/test.fq")  
    for record in test_object:
        assert record[0] is None
        break
   


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    # test if file is blank - raise Error
    with pytest.raises(ValueError):
        parser = FastqParser("tests/blank.fa")
        list(parser)

    # Test general cases (every seq has 3 items: header, sequence, quality)
    test_obj = FastqParser("data/test.fq")
    for record in test_obj:
        assert len(record) == 3  # FASTQ has 3 items (header, seq, quality)
        assert record[0] is not None  # Header exists
        assert record[1] is not None  # Sequence exists
        assert record[2] is not None  # Quality exists
        assert len(record[0]) > 0  # Header is not empty
        assert len(record[1]) > 0  # Sequence is not empty
        assert len(record[2]) > 0  # Quality is not empty

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    test_object = FastqParser("data/test.fa")  
    for record in test_object:
        assert record[0] is None
        break