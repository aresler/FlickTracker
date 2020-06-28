import csv
import json


def get_list(csv_file):
    _list = []
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        r = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in r:
            _list.append(row)
    return _list


def make_dataset(_list):
    dset = []
    i = 1
    while i < len(_list):
        if _list[i][0] != _list[i - 1][0]:
            dset.append(
                {
                    'name': _list[i][0],
                    'alt_name': _list[i][1],
                    'year': _list[i][2],
                    'imdb_rating': _list[i][3],
                    'rating': _list[i][4],
                    'genre': [_list[i][5]],
                }
            )
        else:
            dset[-1]['genre'].append(_list[i][5])
        i += 1
    return dset


def dedup(dset):
    for row in dset:
        row['genre_id'] = list(dict.fromkeys(row['genre_id']))
        row['genre_id'] = list(map(int, row['genre_id']))
        row['platform_id'] = list(dict.fromkeys(row['platform_id']))
        row['platform_id'] = list(map(int, row['platform_id']))
    return dset


def dump_dataset(dset):
    file = open('dataset.json', 'w')
    file.write(json.dumps(dset))
    file.close()


def main():
    _list = get_list('dataset_v2.csv')
    dset = make_dataset(_list)
    # dset = dedup(dset)  # Dedupliate dset
    dump_dataset(dset)


if __name__ == '__main__':
    main()
