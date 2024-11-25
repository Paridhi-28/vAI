import re


def extract_yt_term(command):

    # Define a regular expression pattern to capture the video name 
    pattern = r'play\s+(.*?)\+on\s+youtube'
    
    # Use re.search to find the match in the command
    # re = regular expression
    match = re.search(pattern, command, re.IGNORECASE)

    # If the match is found return the extracted video name, otherwise return None
    return match.group(1) if match else None