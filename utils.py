

def _to_dict_and_cleanup(row):
    dict_row = row.__dict__
    del dict_row["_sa_instance_state"]
    dict_row["created"] = str(dict_row.get("created"))
    return dict_row


def serializer(_list):
    return [_to_dict_and_cleanup(row) for row in _list]
