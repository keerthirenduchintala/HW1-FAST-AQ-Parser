# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    seq = "ATCG"
    result = transcribe(seq)
    assert result == "UAGC"

    seq = "AAATTTCCCGGG"
    result = transcribe(seq)
    assert result == "UUUAAAGGGCCC"

    seq = ""
    result = transcribe(seq)
    assert result == ""


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    seq = "ATCG"
    result = reverse_transcribe(seq)
    assert result == "CGAU"

    seq = "AAATTTCCCGGG"
    result = reverse_transcribe(seq)
    assert result == "CCCGGGAAAUUU"

    seq = ""
    result = reverse_transcribe(seq)
    assert result == ""