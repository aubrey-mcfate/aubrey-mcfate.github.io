def format_label(label):
    if(label == 'puppet'):
        formatted_label = 'Stud Puppet'
    else:
        formatted_label = label.replace("-", " ").title()
    return formatted_label
