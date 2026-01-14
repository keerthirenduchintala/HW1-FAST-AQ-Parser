# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    transcript = ""
    # loop through the seq str and based on key in seq add value to transcript string
    for bp in seq:
        # if bp is not in ALLOWED_NUC add bp, else add the value matching the key in the dictionary
        if bp not in ALLOWED_NUC:
            transcript += bp
        elif bp in TRANSCRIPTION_MAPPING:
            transcript += TRANSCRIPTION_MAPPING[bp]
     # if the read is reversed, reverse
    if reverse:
        transcript = transcript[::-1]
    return transcript
   

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    reverse_transcript = transcribe(seq, True)
    return reverse_transcript