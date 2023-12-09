import pandas as pd


def extract_universities(s: str):
    """
    Extract universities from a string.

    :param s: The string containing university names delimited by parentheses.
    :return: A list of extracted university names.

    Example usage:
    >>> extract_universities("I attended (University of ABC), (University of XYZ), and (University of LMN)")
    ['University of ABC', 'University of XYZ', 'University of LMN']
    """
    unis = []
    l_pars = s.count('(')
    r_pars = s.count(')')
    if r_pars > l_pars: return unis
    start =0
    for i in range(l_pars):
        left = s.find('(')
        right = s.find(')')
        unis.extend(s[left+1: right].split(','))


    return unis


EDIT_TAG = '[edit]'


def read_file(file_path):
    """
    Reads a file and returns its lines
    :param file_path: path to the file
    :return: lines from the file
    """
    with open(file_path, 'r', encoding='UTF-8') as file:
        return file.readlines()


def parse_line(lines):
    """
    Parses lines from the file
    :param lines: lines from the file
    :return: parsed data
    """
    parsed_data = []
    state = ""
    for line in lines:
        if EDIT_TAG in line:
            state = line.replace(EDIT_TAG, "").strip()
        else:
            parenthesis_index = line.find("(")
            city = line[:parenthesis_index].strip()
            universities = extract_universities(line[parenthesis_index:])
            for university in universities:
                parsed_data.append([state, city, university])
    return parsed_data


def clean_data():
    """
    Cleans the data from the 'university_towns.txt' file and returns a pandas DataFrame.
    :return: A pandas DataFrame containing the cleaned data with columns ['State', 'Town', 'University'].
    """
    lines = read_file('Data Sets/university_towns.txt')
    data = parse_line(lines)
    return pd.DataFrame(data, columns=['State', 'Town', 'University'])
