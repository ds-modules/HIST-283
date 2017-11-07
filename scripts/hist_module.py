import random
import pandas as pd
import scipy.stats as scs


def categories(series):
    return range(int(series.min()), int(series.max()) + 1)


def chi_square_of_df_cols(df, col1, col2):

    df[col1] = df[col1].astype('category').cat.codes
    df[col2] = df[col2].astype('category').cat.codes

    df_col1, df_col2 = df[col1], df[col2]

    result = [[sum((df_col1 == cat1) & (df_col2 == cat2))
               for cat2 in categories(df_col2)]
              for cat1 in categories(df_col1)]

    return scs.chi2_contingency(result)


def gen_hex_colour_code():
    return ''.join([random.choice('0123456789ABCDEF')
                    for x in range(6)])  # Make a random string with the letters
    # in the string '0123456789ABCDEF'.


def assign_colors(records_df, col_name):
    color_dict = {}
    for i, c in enumerate(list(set(records_df[col_name]))):
        # We map an institute to a different random color.
        color_dict[c] = "#" + gen_hex_colour_code()
    color_dict

    base_html = '''<tbody><tr>
    <th style="width:25%">Collection</th>
    <th style="width:15%">HEX</th>
    <th style="width:43%">Color</th>
    </tr>
    '''

    add_template = '''
    <tr>
    <td>COLLECTION&nbsp;</td>
    <td>HEX</td>
    <td style="background-color:HEX">&nbsp;</td>
    </tr>
    </tbody>
    '''

    to_render = base_html

    for k in color_dict.keys():
        to_render += add_template.replace(
            'COLLECTION', k).replace(
            'HEX', color_dict[k])

    to_render += '</tbody>'
    to_render = to_render.replace('Collection', col_name)

    return (color_dict, to_render)
