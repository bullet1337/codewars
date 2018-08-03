# https://www.codewars.com/kata/567fe8b50c201947bc000056
def ipv4_address(address):
    parts = address.split('.')
    if len(parts) != 4:
        return False
        
    return all(part.isdigit() and (len(part) == 1 or part[0] != '0') and 0 <= int(part) <= 255 for part in parts)